from bs4 import BeautifulSoup
import requests as req

def find_title(soup):
    movietitle = soup.select('.h_movie > a')[0].text
    return movietitle

def find_outlines(soup):
    movieoutlines = soup.select('.info_spec > dd > p > span')[0]
    outlines = []
    for outline in movieoutlines:
        outline = outline.text
        outline = outline.strip()
        if outline == '':
            continue
        outlines.append(outline)

    return ''.join(outlines)

def find_director(soup):
    moviedirector = soup.select('.info_spec > dd > p > a')[0].text
    return moviedirector

def find_grade(soup):
    moviegrade = soup.select('.st_on')[0].text
    return moviegrade

def find_main_module(url):
    res = req.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    title = find_title(soup)
    outlines = find_outlines(soup)
    director = find_director(soup)
    grade = find_grade(soup)
    
    return(title, outlines, director, grade)
