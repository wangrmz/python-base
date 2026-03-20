import aiohttp
import asyncio


async def download_picture(session, url):
    print(f'开始下载:{url}')
    # 发送网络请求，获取这张图片,请求发出去后，要等待服务器把数据返回，等的这段时间就是IO等待
    response = session.get(url)
    # 等待数据（图片数据可能分多次传输，需要等待数据全部读完，等的这段时间也是IO等待
    content = await response.read()
    print('下载完毕')
    # 保存图片到本地
    with open(url[-10:], 'wb') as f:
        f.write(content)
    # 释放链接资源
    await  response.release_conn()


async def main():
    url_list = [
        'https://image.baidu.com/search/detail?adpicid=0&b_applid=10742240618174679096&bdtype=0&commodity=&copyright=&cs=2961979787%2C2118568161&di=7609719975837696001&fr=click-pic&fromurl=http%253A%252F%252Fmbd.baidu.com%252Fnewspage%252Fdata%252Fdtlandingsuper%253Fnid%253Ddt_4479421423332807657&gsm=1e&hd=&height=0&hot=&ic=&ie=utf-8&imgformat=&imgratio=&imgspn=0&is=254054932%2C3706235438&isImgSet=&latest=&lid=9f20886a003a3efe&lm=&objurl=https%253A%252F%252Fgips3.baidu.com%252Fit%252Fu%253D2961979787%252C2118568161%2526fm%253D3074%2526app%253D3074%2526f%253DPNG%253Fw%253D2560%2526h%253D1440&os=254054932%2C3706235438&pd=image_content&pi=0&pn=0&rn=1&simid=4221623712%2C396016385&tn=baiduimagedetail&width=0&word=%E5%A3%81%E7%BA%B8&z='
        'https://image.baidu.com/search/detail?adpicid=0&b_applid=10742240618174679096&bdtype=11&commodity=&copyright=&cs=3364344117%2C1410407837&di=46137345&fr=click-pic&fromurl=http%253A%252F%252Fweibo.com%252F7765267012%252FQlHKxtjbf&gsm=1e&hd=&height=0&hot=&ic=&ie=utf-8&imgformat=&imgratio=&imgspn=0&is=0%2C0&isImgSet=&latest=&lid=9f20886a003a3efe&lm=&objurl=https%253A%252F%252Fww3.sinaimg.cn%252Fmw690%252F008twgG8gy1i8zu1oeno2j30kg10cn1v.jpg&os=2954398064%2C1638095026&pd=image_content&pi=0&pn=1&rn=1&simid=3364344117%2C1410407837&tn=baiduimagedetail&width=0&word=%E5%A3%81%E7%BA%B8&z=',
        'https://image.baidu.com/search/detail?adpicid=0&b_applid=10742240618174679096&bdtype=11&commodity=&copyright=&cs=1629550397%2C1909442722&di=46137345&fr=click-pic&fromurl=http%253A%252F%252Fweibo.com%252F2819647710%252FQlOSvBJch&gsm=1e&hd=&height=0&hot=&ic=&ie=utf-8&imgformat=&imgratio=&imgspn=0&is=0%2C0&isImgSet=&latest=&lid=9f20886a003a3efe&lm=&objurl=https%253A%252F%252Fww2.sinaimg.cn%252Fmw690%252Fa81068dely1i90pi5x1j1j210o27o4qp.jpg&os=1006801398%2C3187953147&pd=image_content&pi=0&pn=7&rn=1&simid=1629550397%2C1909442722&tn=baiduimagedetail&width=0&word=%E5%A3%81%E7%BA%B8&z=']

    # 创建会话对象（请求的工具）
    session = aiohttp.Session()
    # 创建多个协程对象
    coroutine_list = [download_picture(session, url) for url in url_list]
    # 将多个协程对象交给事件循环，拆包
    await asyncio.gather(*coroutine_list)
    # 关闭会话
    await session.close()


# 启动下载
asyncio.run(main())
