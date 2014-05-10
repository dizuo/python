#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <GL/glut.h>
#include <cmath>
#include <ctime>

//#include "BezierLinkRender.h"
#include "RoundBoxRender.h"

//////////////////////////////////////////////////
//global
enum ColorIndex
{
	red, crimson, violet, orange, yellow, glod, green, lightgreen,
	darkgreen, olivegreen, blue, darkblue, royalblue, skyblue, midnightbue, 
	fuchsia, aqua, pink, salmonpink, turquoise, darkturpuoise, gray, lightgray, darkgray
};

struct DataCfg
{
	int labelxpos;
	int labelypos;
	int headxpos;
	int headypos;
};

void getCfg(const char* fname, DataCfg* pcfg);  

GLuint gColorStable[] =
{
	(0xFF0000),	//red 
	(0xDC143C),	//crimson
	(0x9400D3),	//violet
	(0xFFA000),	//orange
	(0xFFFF00),	//yellow
	(0xFFD700),	//glod
	(0x00FF00),	//green
	(0x90FF90),	//lightgreen
	(0x006400),	//darkgreen
	(0x556B2F),	//olivegreen		//very good color?¨¬¨¦?¨¦-
	(0x0000FF),	//blue
	(0x00008B),	//darkblue
	(0x4169E1),	//royalblue
	(0x5555FF),	//skyblue
	(0x191970),	//midnightbue
	(0xFF00FF),	//fuchsia
	(0x00FFFF),	//aqua
	(0xffb6c1),	//pink
	(0xFF91A4),	//salmonpink
	(0x30D5C8),	//turquoise
	(0x008080),	//darkturpuoise
	(0xA9A9A9),	//gray
	(0xD3D3D3),	//lightgray
	(0x808080)	//darkgray
};

float g_fWidth = 500;
float g_fHeight = 500;
float g_fDepth = 100;
float g_fAngle = .0;
int g_workArr[31] = { 0 };

DataCfg g_cfg;

int		gRoundboxtype = 0;
//////////////////////////////////////////////////////////////////////////
void renderBitmapString2D(float x, float y, void *font, char *string);
void getColorFromTable(GLuint rgb, float vec[3]);
void getWorkTime(const char* fname, int(&arr)[31]);

void init(void)
{
	RoundBoxRender::setType(gRoundboxtype);
	printf("%d\n", gRoundboxtype);	
	getWorkTime("work_time.txt", g_workArr);
	getCfg("cfg.txt", &g_cfg);

	glClearColor(0.9, 0.9, 0.9, 0.0);
	glShadeModel(GL_SMOOTH);
}

void display(void)
{
	const float slotSize = 30.f;
	const float slotColor[] = { 0.8f, 0.8f, 0.8f };
	const float slotShadowSize = 2.0f;
	const float slotShadowAlpha = 0.7;

	glClear(GL_COLOR_BUFFER_BIT);
	glColor3f(1.0, 1.0, 1.0);

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	glOrtho(0, g_fWidth, 0, g_fHeight, 0, g_fDepth);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();

	glTranslatef(50.0, 50.f, 0.f);		// Ô­µã×óÏÂ½Ç¡£

	int xPos(0);
	int yPos(0);
	int xOffset(0);
	int yOffset(0);

	const float kRectSize = 40;
	const float kOffset = 50.0f;
	const int kRowSize = 7;
	const int kColSize = 6;
	// const char* kHeaderInfo = "mtwtfss";
	const char* kHeaderInfo = "MTWTFSS";
	const int kCommonColorIndex = 5;
	int counter = 1;

	glPushMatrix();

	for (int i = 0; i < 42; i++)
	{
		float colorVec[3];	
		getColorFromTable(gColorStable[kCommonColorIndex], colorVec);
		glColor3fv(colorVec);
		RoundBoxRender::setType(i % kRowSize);

		yOffset = i % kRowSize;
		xOffset = i / kRowSize;

		char buffer[10] = { 0 };
		int fontWidOffset = 5;
		int fontHghOffset = 10;

		if (xOffset == 0)
		{
			buffer[0] = kHeaderInfo[6 - i];
		}
		else if (xOffset > 1 || yOffset < 6)
		{
			int height = xOffset == 1 ? 5 : 6;
			int xbaseArr[] = { 0, 1, 7, 14, 21, 28 };			
			int datVal = xbaseArr[xOffset] * 2 + height - counter;

			if (datVal < 31)
			{
				_itoa(datVal, buffer, 10);
				fontWidOffset = datVal>10 ? 12 : 5;

				// Change the color
				int workOffHour = g_workArr[datVal];
				int colorIndex = kCommonColorIndex;

				switch (workOffHour)
				{
				case 18:
					colorIndex = lightgreen;		// D 18 - 19	
					break;		
				case 19:
					colorIndex = darkgreen;		// C 19 - 20
					break;
				case 20:
					colorIndex = skyblue;		// B 20 - 21
					break;
				case 21:
					colorIndex = blue;		// A 21 - 22
					break;
				case 22:
					colorIndex = red;			// S 22 - 23	
				default:
					break;
				}

				getColorFromTable(gColorStable[colorIndex], colorVec);
				glColor3fv(colorVec);
			}

			++counter;
		}

		glPushMatrix();
		{
			glTranslatef(xPos + xOffset * kOffset, yPos + yOffset * kOffset, 0.f);
			RoundBoxRender::gl_round_box_shade(GL_POLYGON, 0, 0, kRectSize, kRectSize, 10, 0.3, 0);
			
			glColor3f(0.f, 0.f, 0.0f);
			renderBitmapString2D(kRectSize / 2 - fontWidOffset, kRectSize / 2 - fontHghOffset, GLUT_BITMAP_TIMES_ROMAN_24, buffer);
		}glPopMatrix();
	}
	glPopMatrix();

	int labelColorIdxArr[] = {lightgreen, darkgreen, skyblue, blue, red};
	char* labelInfo[] = { "18:00-19:00", "19:00-20:00", "20:00-21:00", "21:00-22:00", "22:00-23:00" };

	xPos = g_cfg.labelxpos;
	yPos = g_cfg.labelypos;
	yOffset = 30;
	for (int i = 0; i < sizeof(labelColorIdxArr)/sizeof(labelColorIdxArr[0]); i++)	
	{
		char* str = labelInfo[i];

		int fontWidOffset = 10;
		int fontHghOffset = 10;

		int boxSize = 30;

		float colorVec[3];
		getColorFromTable(gColorStable[labelColorIdxArr[i]], colorVec);
		glColor3fv(colorVec);
		RoundBoxRender::setType(0);

		glPushMatrix();
		{
			glTranslatef(xPos, yPos + i * yOffset, 0.f);
			RoundBoxRender::gl_round_box_shade(GL_POLYGON, 0, 0, boxSize*3.2, boxSize, 10, 0.3, 0);
			glColor3f(0.f, 0.f, 0.0f);
			renderBitmapString2D(boxSize / 2 - fontWidOffset, boxSize / 2 - fontHghOffset, GLUT_BITMAP_TIMES_ROMAN_24, str);
		}glPopMatrix();
	}
	//glColor3f(1.0f, 1.0f, 0.0f);
	//ui_draw_link_bezier(&gRect);

	char* head = "2014-04-OffWorkTime [dizuo]";
	float colorVec[3];
	getColorFromTable(gColorStable[darkblue], colorVec);
	glColor3fv(colorVec);
	glPushMatrix();
	{
		glTranslatef(g_cfg.headxpos, g_cfg.headypos, 0);
		renderBitmapString2D(0, 0, GLUT_BITMAP_TIMES_ROMAN_24, head);

	} glPopMatrix();
	
	glutSwapBuffers();
}

void reshape(int w, int h)
{
	glViewport(0, 0, (GLsizei)w, (GLsizei)h);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluPerspective(60, 1.0, 1.5, 20);
	glMatrixMode(GL_MODELVIEW);
}

void keyboard(unsigned char key, int x, int y)
{
	switch (key)
	{
	case 27:
		exit(0);
		break;
	}
	glutPostRedisplay();
}

void mouse(int button, int state, int x, int y)
{
	if (button == GLUT_LEFT_BUTTON)
		switch (state)
	{
		case GLUT_DOWN:
			break;

		case GLUT_UP:
			break;
	}
	glutPostRedisplay();
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
	glutInitWindowSize(700, 700);
	glutInitWindowPosition(100, 100);
	glutCreateWindow(argv[0]);
	init();
	glutDisplayFunc(display);
	glutReshapeFunc(reshape);
	glutKeyboardFunc(keyboard);
	glutMouseFunc(mouse);
	glutMainLoop();
	return 0;
}

void renderBitmapString2D(float x, float y, void *font, char *string)
{
	if (!string || strlen(string) == 0)
	{
		return;
	}

	char *c;
	// set position to start drawing fonts
	glRasterPos2f(x, y);
	// loop all the characters in the string
	for (c = string; *c != '\0'; c++) {
		glutBitmapCharacter(font, *c);
	}
}
void getColorFromTable(GLuint rgb, float vec[3])
{
	GLubyte  r = GLubyte((rgb >> 16) & 0xFF);
	GLubyte  g = GLubyte((rgb >> 8) & 0xFF);
	GLubyte  b = GLubyte(rgb & 0xFF);
	vec[0] = r / 255.0f;
	vec[1] = g / 255.0f;
	vec[2] = b / 255.0f;
}

void getCfg(const char* fname, DataCfg* pcfg)
{
	FILE* fp = fopen(fname, "r");
	if (!fp)
	{
		return;
	}

	char buffer[512];
	const char* token = " =";

	while (fgets(buffer, 512, fp))
	{
		if (strlen(buffer) < 2)
		{
			break;
		}

		if (buffer[0] == '#')
		{
			continue;
		}

		char* pch = strtok(buffer, token);
		char tag[100] = { 0 };
		strncpy(tag, pch, 100);

		pch = strtok(NULL, token);
		
		if (strcmp(tag, "labelxpos") == 0)
		{
			pcfg->labelxpos = atoi(pch);
		}
		else if (strcmp(tag, "labelypos") == 0)
		{
			pcfg->labelypos = atoi(pch);
		}
		else if (strcmp(tag, "headxpos") == 0)
		{
			pcfg->headxpos = atoi(pch);
		}
		else if (strcmp(tag, "headypos") == 0)
		{
			pcfg->headypos = atoi(pch);
		}

	}
}

void getWorkTime(const char* fname, int(&arr)[31])
{
	FILE* fp = fopen(fname, "r");
	if (!fp)
	{
		return;
	}

	int count = 0;
	char buffer[1024];
	while (fgets(buffer, 1024, fp))
	{
		if (strlen(buffer) < 2)
		{
			break;
		}

		int year;
		int month;
		int day;
		int hour;
		int minute;
		sscanf(buffer, "%d-%02d-%02d %d:%d", &year, &month, &day, &hour, &minute);

		arr[day] = hour;
		// 2014-04-01 21:20
	}

}