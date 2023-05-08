import concurrent.futures
# import multiprocessing
import requests


def downloadFile(url,name):
    res = requests.get(url)
    open(f"files/file{name}.jpg", "wb").write(res.content)

    #long process
# if __name__ == '__main__':

    # url = "https://picsum.photos/2000/3000"
#     pros = []

#     for i in range(5):
#         downloadFile(url,i)
#         p = multiprocessing.Process(target=downloadFile,args=[url,i])
#         p.start()
#         pros.append(p)

#     for p in pros:
#         p.join()

if __name__ == '__main__':
    url = "https://picsum.photos/2000/3000"

    with concurrent.futures.ProcessPoolExecutor() as executor:
        l1 = [url for i in range(10)]
        l2 = [i for i in range(10)]
        result = executor.map(downloadFile, l1, l2)
        for r in result:
            print(r)