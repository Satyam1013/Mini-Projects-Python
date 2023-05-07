import asyncio
import requests


async def func1():
  print(1)
  URL = "https://www.clearwallpaper.com/wp-content/uploads/2020/03/4k-wallpapers-9.jpg"
  response = requests.get(URL)
  open("ice.jpg", "wb").write(response.content)
  return 'Done 1'


async def func2():
   print(2)
   URL = "https://cdn.wallpapersafari.com/16/65/FjdTtm.jpg"
   response = requests.get(URL)
   open("sunset.jpg", "wb").write(response.content)


async def func3():
   print(3)
   URL = "https://res.cloudinary.com/kamiltech-com/image/upload/v1478182715/Wallpapers/Set-1/3.jpg"
   response = requests.get(URL)
   open("success.jpg", "wb").write(response.content)

async def main():
#   await func1()
#   await func2()
#   await func3()
  x = await asyncio.gather(func1(),func2(),func3())
  print(x)


asyncio.run(main())


# await func1()
# await func2()
# await func3()
