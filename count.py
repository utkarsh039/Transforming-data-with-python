if __name__=="__main__":
    import pandas as pd
    import read
    import collections
    
    hn_stories=read.load_data()             # data is read from inbuilt dataset
    headline_str=""                         # empty string is set
    for i in hn_stories["headline"]:  
        headline_str=headline_str+str(i)    #string is appended
    headline_str= str.lower(headline_str)   # change to lowe case
    data=headline_str.split(" ")
    print(collections.Counter(data).most_common(100))  # return the result
