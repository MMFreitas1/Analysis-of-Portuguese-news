__Disclaimer__: This project is intended for educational purposes only. Under no circumstances should the content be used, replicated, or distributed without the explicit authorization of the author.

Run install_packages files via Anaconda

Thanks to Rafael Almeida for creating LeIA library, essentialy using the power of NLTK's VADER module to measure sentiment in Portuguese

@misc{Almeida2018,
  author = {Almeida, Rafael J. A.},
  title = {LeIA - Léxico para Inferência Adaptada},
  year = {2018},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/rafjaa/LeIA}}
}

This research project comprehends a time window of analysis from 16Jan2024 to 16Jan2025, where portuguese news are downloaded from a news corporation through a web scraping script and analysed from time to time with an analysis script containing nlp workflows. The objectives of the project at the momement envelop: 


1) Analysis of most used words
2) Comprehensive sentiment analysis of Portuguese news
* Compare news categories
* Sentiment time-series exploratory research
* Analyze political party sentiment
* Correlation with weather
* Check if titles are more negative to create an impression
3) Analyze which soccer club was spoken about the most

There is a github workflow in due corse, that automatically activates the web-scraping script every day @ 7p.m.

Although the scope of the project was intended to be just one year, the web scraping workflow is active for future use.

*Note*: Chromadb files are ignored in this repository for simplicity