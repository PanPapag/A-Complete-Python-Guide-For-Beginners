"""
    Remember that none of these methods can ever change or mutate the original
    string, they can only produce a new one based on the old one
"""

s  = "Hello World"
print(s.upper())

t = s.lower()

print(t)
print(s)

ss = "    Hello, World    "

els = ss.count("l")
print(els)

print("***"+ss.strip()+"***")       # strip remove white spaces both in the beginning
                                    # and in th end

news = ss.replace("o", "***")       # replace o with ***
print(news)
