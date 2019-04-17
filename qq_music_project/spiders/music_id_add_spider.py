# -*- coding: utf-8 -*-
import scrapy
import json


from qq_music_project.items import QqMusicProjectItem

class MusicIdAddSpiderSpider(scrapy.Spider):
    name = "music_id_add_spider"
    def start_requests(self):
        # 每次启动爬虫程序首先读取xxx.txt文件转为int类型作为起始id，之后每次循环把id写入此文件（覆盖）可以抓取数量可以自己拟定
        with open('./xxx.txt', 'r')as f:
            start_music_id = f.readline()
        for i in range(int(start_music_id),int(start_music_id)+150000):
            with open('./xxx.txt', 'w')as x:
                x.write(str(i+1))
            url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?data={"comm":{"format":"json","g_tk":5381,"inCharset":"utf-8","needNewCode":0,"notice":0,"outCharset":"utf-8","platform":"h5"},"songinfo":{"method":"get_song_detail","param":{"song_type":0,"song_mid":"","song_id":'+str(i)+'},"module":"music.pf_song_detail_svr"}}'
            yield scrapy.Request(url,self.music_detail_parse,meta={'track_id':i})

    def music_detail_parse(self,response):
        track_id = response.meta['track_id']
        music_detail_json = json.loads(response.text)
        music_info = music_detail_json['songinfo']['data']['info']
        music_track_info = music_detail_json['songinfo']['data']['track_info']
        music_extras = music_detail_json['songinfo']['data']['extras']

        track_info_id = music_detail_json['songinfo']['data']['track_info']['id']
        track_info_time_pub = music_detail_json['songinfo']['data']['track_info']['time_public']
        if track_id == track_info_id and track_info_time_pub != '':
            item = QqMusicProjectItem()
            item['id'] = track_info_id
            item['track_info'] = music_track_info
            item['info'] = music_info
            item['extras'] = music_extras
            yield item
        else:
            with open('null_id.txt','a+')as f:
                f.write(str(track_id)+'\n')
