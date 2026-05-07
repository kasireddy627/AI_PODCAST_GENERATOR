from newspaper import Article


def extract_article(url: str):
    try:
        article = Article(url)

        article.download()
        article.parse()

        if len(article.text) < 200:
            return {
                "error": "Extraction failed or article too short"
            }

        article.nlp()

        return {
            "title": article.title,
            "authors": article.authors,
            "text": article.text,
            "summary": article.summary
        }

    except Exception as e:
        return {
            "error": str(e)
        }