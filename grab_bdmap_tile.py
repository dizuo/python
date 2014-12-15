# -*- coding: cp936 -*-
import math

def lonlat2Mercator(x,y):
    '''
    ��γ��תī��������
    x: ����
    y: γ��
    89.808�Ǳ�΢��ľ���--__--! ллxgsongָ��
    '''
    x = x * 20037508.34 / 180.0
    y = math.log(math.tan((89.808 + y) * math.pi / 360.0)) / (math.pi / 180.0)
    y = y * 20037508.34 / 180.0
    return x,y

def tile_index(lon,lat,z):
    '''
    ��γ��ת���ڼ���z����Ƭ���
    lon: ����
    lat: γ��
    z: ��ͼ����
    '''
    lon,lat = lonlat2Mercator(lon,lat)
    lon = lon / math.pow(2.0,(18 - z))
    lat = lat / math.pow(2.0,(18 - z))
    x = int (lon / 256.0)
    y = int (lat / 256.0)
    return x,y

lon=116.403802
lat=39.915198
z=18
x,y = tile_index(lon,lat,z)
tile_url = "http://online2.map.bdimg.com/tile/?qt=tile&x=%d&y=%d&z=%d&styles=pl&udt=20140928" % (x,y,z)
print tile_url
