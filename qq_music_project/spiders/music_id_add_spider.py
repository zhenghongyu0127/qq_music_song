# -*- coding: utf-8 -*-
import scrapy
import json


from qq_music_project.items import QqMusicProjectItem

class MusicIdAddSpiderSpider(scrapy.Spider):
    name = "music_id_add_spider"
    def start_requests(self):
        start_music_id = input('请输入起始ID！')
        end_music_id = input('请输入结束ID！')
        for i in range(int(start_music_id),int(end_music_id)):
            url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?data={"comm":{"ct":24,"cv":0},"songinfo":{"method":"get_song_detail_yqq","param":{"song_type":0,"song_mid":"","song_id":'+str(i)+'},"module":"music.pf_song_detail_svr"}}'
            yield scrapy.Request(url,self.music_detail_parse)

    def music_detail_parse(self,response):
        music_detail_json = json.loads(response.text)
        music_info = music_detail_json['songinfo']['data']['info']
        music_track_info = music_detail_json['songinfo']['data']['track_info']

        item = QqMusicProjectItem()
        item['music_info'] = music_info
        item['music_track_info'] = music_track_info
        yield item
