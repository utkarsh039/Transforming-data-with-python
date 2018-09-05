if __name__=="__main__":
    import pandas as pd
    import read
    import collections
    
    hn_stories=read.load_data()
    headline_str=""
    for i in hn_stories["headline"]:
        headline_str=headline_str+str(i)
    headline_str= str.lower(headline_str)
    data=headline_str.split(" ")
    print(collections.Counter(data).most_common(100))