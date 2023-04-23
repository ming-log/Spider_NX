# -- coding: utf-8 --
"""
@Name: demo3_百度翻译.py
@Auth: Ming-Log
@Date: 2023/4/12-0:32
@Desc: 
"""
import requests
import execjs


def translation(query):
    with open('demo3_百度翻译.js', 'r', encoding='utf-8') as f:
        jscode = f.read()

    sign = execjs.compile(jscode).call('exports', query)
    print('sign:', sign)
    url = 'https://fanyi.baidu.com/v2transapi'

    params = {
        'from': 'zh',
        'to': 'en'
    }

    data = {
        'from': 'zh',
        'to': 'en',
        'query': query,
        'simple_means_flag': '3',
        'sign': sign,
        'token': '5e24d68bbbdfd67c16b35da74870b8f5',
        'domain': 'common'
    }

    headers = {
        'Acs-Token': '1681207459572_1681230773001_6QSOvqBC30fj/DQlqEHLbEvR+KrHKmhInuV8Ev4NwvcvSmhn2lmdHi9zQLT3FMr6hQ90PYdWlv1+emb56TiUxmh5twktLTwAJkxoibo7szZXlBzrV+6eGjTtpwVYEESHy7xZZbBg5ChSim6zY/3Z0MBkFj7MBAxkzDo041Oh7qIc9IfMaqM+X0Qkjjrq9YajZq5WFRVsNQCobhGC19EDNjFHXDMKqxoiihwAwKl0EWQ5aFBMua+1D88+QNY/nbNZs0UY/4zjG1DHuTKpoC8TcJwKO6LccQcVQomtJd3Tzz+QYN0wvo1+t/eOnI9WC0R4BLuCkDNX55nL/sj9NuNam+d8FoG5fPAF99OtctZ/ZLUijwIJFrswDFAquSf6skz/cnFkkOpbU7WUoJzVwvzOQN7hdCRt9/+QGcOhp0r3FYMzvgOOXlhjLkFPGo+xXaTEbNqf/bolzV6zJQJwl+XOOfvZNTHusz/DZ2ByNRJc71A=',
        'Origin': 'https://fanyi.baidu.com',
        'Host': 'fanyi.baidu.com',
        'Referer': 'https://fanyi.baidu.com/',
        'Cookie': 'BIDUPSID=640EA7E3BAD4E8112A3F37BAE453FFC0; PSTM=1636376597; __yjs_duid=1_eca79fd06ced9005d3e42161ced1be071636376605131; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; REALTIME_TRANS_SWITCH=1; APPGUIDE_10_0_2=1; BAIDUID=E3F1FC1FB03A5813D138C43F88580D57:FG=1; newlogin=1; BDUSS=jJnTjRpfmNDQ1RGcmJiMjdPYXFxc0ZaMFNTSEh-NThOYkRIQ1pWanl1MXU0VnhrSVFBQUFBJCQAAAAAAAAAAAEAAAD-I3~psK7Jz7XItcg1MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG5UNWRuVDVkV; BDUSS_BFESS=jJnTjRpfmNDQ1RGcmJiMjdPYXFxc0ZaMFNTSEh-NThOYkRIQ1pWanl1MXU0VnhrSVFBQUFBJCQAAAAAAAAAAAEAAAD-I3~psK7Jz7XItcg1MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG5UNWRuVDVkV; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1679319681,1679486289,1681228994; H_PS_PSSID=26350; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; delPer=0; PSINO=7; BAIDUID_BFESS=E3F1FC1FB03A5813D138C43F88580D57:FG=1; BA_HECTOR=aha4ak248ha08l25000h21eu1i3b1td1m; ZFY=TBLf32wVkw2ixDINRGBUdQj9:BnfLyrnFQHzsixPgdaM:C; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1681230773',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    res = requests.post(url, params=params, data=data, headers=headers)
    return res.json()['trans_result']['data'][0]['dst']


if __name__ == '__main__':
    query = '你好啊，我觉得今天天气不错！我们出去露营吧。'
    trans = translation(query)
    print('-' * 50)
    print(f'{query}\n翻译为:\n{trans}')
    print('-' * 50)
