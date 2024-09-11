Programiranje za web

Izrada: Kovačev Antonio

Tema projekta: Novinski portal

Modeli: News, Author, Category

News reprezentira članke sa atributima naslov, tekst članka, datum objave, te vanjske ključeve autor i kategorija

Author reprezentira novinare sa atributima ime, prezime, email i broj telefona novinara

Category reprezentira nazive kategorija sa atributom category_name

Svi podaci se unose sa Faker metodom preko make_data.py datotekom koja se nalazi na putanji main/management/commands

Web sjedište se sastoji od 3 stranice. index.html predstavlja naslovnu stranicu na putanji :8000/ news_list.html predstavlja stranicu "Vijesti" sa ispisom naslova članka, teksta članka, autorom članka, te datumom objave članka na putanji :8000/news authors_list.html predstavlja stranicu "Novinari" sa ispisom imena i prezimena svih novirana, njihov pripadajući mail, te telefonski broj na putanji 8000:/authors

