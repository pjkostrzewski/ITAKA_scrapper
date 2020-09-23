# ITAKA_scrapper
Best offers from ITAKA travel agency [website](https://www.itaka.pl)\
Technologies: Python 3.8, Django Rest Framework, Celery, BeautifulSoup4

- [X] data scraper
- [X] REST API
- [ ] periodic task to update data (Celery)
- [ ] Docker
- [ ] frontend


# RESULTS
3689zł -> 1099zł  (-70%)  |  4.7  |  Grecja\
3739zł -> 1199zł  (-67%)  |  4.5  |  Grecja\
3789zł -> 1299zł  (-65%)  |  5.2  |  Grecja\
3149zł -> 1399zł  (-55%)  |  4.4  |  Madera\
4081zł -> 1441zł  (-64%)  |  4.6  |  Grecja\
4389zł -> 1799zł  (-59%)  |  5.0  |  Grecja\
3389zł -> 1799zł  (-46%)  |  5.0  |  Grecja\
3449zł -> 1799zł  (-47%)  |  4.7  |  Madera\
3749zł -> 1799zł  (-52%)  |  4.9  |  Madera\
3939zł -> 1899zł  (-51%)  |  5.4  |  Grecja\
3949zł -> 1899zł  (-51%)  |  4.9  |  Madera\
3949zł -> 1899zł  (-51%)  |  4.5  |  Madera\
3549zł -> 1899zł  (-46%)  |  5.2  |  Madera\
3809zł -> 2159zł  (-43%)  |  4.8  |  Wyspy Kanaryjskie\
4209zł -> 2249zł  (-46%)  |  5.0  |  Wyspy Kanaryjskie\
4409zł -> 2349zł  (-46%)  |  5.1  |  Wyspy Kanaryjskie\
4209zł -> 2449zł  (-41%)  |  0  |  Wyspy Kanaryjskie\
4609zł -> 2549zł  (-44%)  |  5.2  |  Wyspy Kanaryjskie\
4309zł -> 2639zł  (-38%)  |  5.3  |  Wyspy Kanaryjskie\
5209zł -> 3029zł  (-41%)  |  5.5  |  Wyspy Kanaryjskie\
5109zł -> 3129zł  (-38%)  |  5.8  |  Wyspy Kanaryjskie\
5349zł -> 3199zł  (-40%)  |  5.5  |  Madera

# EXAMPLE JSON VIEW

{\
        "offer_id": "78fbc334d4f2958de8f4ffdb300b60adb4cb0456687f6068fee0b12d6690e6d0",\
        "destination": "Grecja",\
        "old_price": 3689,\
        "current_price": 1099,\
        "rank": 4.7,\
        "link": <link\>\
    },
