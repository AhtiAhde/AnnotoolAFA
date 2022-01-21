# Requirements Document

## Vertaisarviointia varten

Idea on ottaa kirjoja tekstinä sisään, pilkkoa ne 500 sanan ikkunoiksi perustuen suurinpiirtein kappalejakoihin. Näistä olisi sitten ideana rakentaa priorisoitu lista käyttäen [tämän (Hu et. al. 2020) paperin][4] esittelemiä menetelmiä ja mahdollisesti kokeilla sentimentti sanastojen sijaan myös muita mahdollisia sanastoja, jotka perustuvat isommassa projektissa käyttämiini kirjoitusteorioihin.

## Larger Context

I have been researching the problem of “How AI could understand dramatic arcs of narratives” since 2016. While BERT and GPT-3 like systems have been used for computational creativity by utilizing the generative features of the language models, the results are generally uninteresting and they need humans to cherry pick the good artifacts from the uninteresting ones; in other words, the creativity is based on hermeneutic circle rather than statistical reliability. The ability of large language models to understand semantic meanings have been largely contested, for example in [here][1] and [here][2]. I have reviewed +8 writing theories used by professional fiction writers and Hollywood in general. My basic thesis is that by modeling the artifacts used by professional fiction writers and annotating those in existing fiction productions, we might be able to develop a narrative model that would be able to understand the difference between text and subtext.

According to the [Narrating Complexity journal by Richard Walsh][3], narratives have local artifacts that have global effects. Adaptive Fractal Analysis is able to detect such structures from data. The method first divides the data to windows of static size and then calculates the change of frequency of specific events. For example, in 2020 a research group [used this method][4] to analyze sentiment codeword frequency in text windows in order to detect the dramatic highlights of a story. The results were successfully in line with literature experts. However, the book was chosen specifically for this purpose as the sentiment reflected well the dramatic arc of the book as the theme of the book was sentimental itself. Thus this very same method might not work for all works of fiction.

## In this project

In order to generalize this model, I have built a framework by using three fractal writing theories (which consider writing as a complex process of repetition and permutation of specific subtext artifacts at different scales). Instead of relying only on sentiment I am able to build dictionaries and / or language models related to these writing theories, that would then allow me to extract and regenerate many different high-drama points from fictional stories with high probability. These would form the micro-level text artifacts that would offer a Bellman Equation for constructing the macro-level subtext structures, which [according to Walsh][3] are key for tackling the complexity of narratives.

In order to build the language models, I need annotated data. However, books are sparse of interesting dramatic events related to the framework I have built and thus crowdsourcing would turn out inefficient. In order to improve the density of the interesting dramatic events I would need a way to prioritize the paragraphs of a book by their probability for containing interesting dramatic events. The Adaptive Fractal Analysis of sentiments could help in this problem and by using non-sentiment based dictionaries, the quality of the solution could be improved further.

The goal of this project is to use Adaptive Fractal Analysis to produce a prioritized list of interesting dramatic events in any book of fiction (or if this turns out too hard of a problem, then first within a specific genre). I will be using the sentiment dictionary as a starting point and then try to extend the process to do multiple parallel analysis based on [MICE quotient by Mary Robinette Kowal][8] and [Promises, Progresses and Payoffs-framework by Brandon Sanderson][9]. If I have time I might also try extending to a subset of [Dramatica][10] (it has 196 features as opposed to 4 and 3 of the other two, so I would not do all of them now; I have a pseudo automated way for building the dictionaries, which I used in 2018 for another project).

## Important Technical Aspects

I will do this project with Python. The inputs in this project will be books. They will be split into paragraphs or segments of text that are approximately 500 tokens long (I will later use the annotations with BERT). The output thus would be a prioritized list of such segments.  I have already implemented a script for fetching relevant project Gutenberg books and a database where to store the text artifacts for future annotation. The process will be run as a background process with no significant real-time requirements. I am not certain about the time complexity of Adaptive Fractal Analysis, but I would guess it to be around O(n log n); the memory footprint is also expected (but not required) to be very low.

## Course Related Stuff

I am part of the TKT study program and the language used will be english. I am able to peer-review Golang, PHP, JavaScript and Python.

## References

1: What does it mean for AI to Understand: https://www.quantamagazine.org/what-does-it-mean-for-ai-to-understand-20211216/

2: Limitations of scaling up AI language models: https://venturebeat.com/2021/12/10/the-limitations-of-scaling-up-ai-language-models/

3: Narrating Complexity: https://www.academia.edu/39366860/Narrative_Theory_for_Complexity_Scientists

4: Dynamic evolution of sentiments in Never Let Me Go: Insights from multifractal theory and its implications for literary analysis: https://academic.oup.com/dsh/article/36/2/322/5856850

5: A tutorial introduction to adaptive fractal analysis: https://www.researchgate.net/publication/232236967_A_tutorial_introduction_to_adaptive_fractal_analysis

6: Fractal Analysis of Time-Series Data Sets: Methods and Challenges: https://www.intechopen.com/chapters/64463

7: Detrended Fluctuation Analysis and Adaptive Fractal Analysis of Stride Time Data in Parkinson's Disease: Stitching Together Short Gait Trials: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0085787

8: MICE quotient: https://www.youtube.com/watch?v=blehVIDyuXk

9: Promises, Progresses, Payoffs: https://www.youtube.com/watch?v=0cf-qdZ7GbA&list=PLSH_xM-KC3Zv-79sVZTTj-YA6IAqh8qeQ

10: Dramatica: https://dramatica.com/theory/book

[1]: https://www.quantamagazine.org/what-does-it-mean-for-ai-to-understand-20211216/

[2]: https://venturebeat.com/2021/12/10/the-limitations-of-scaling-up-ai-language-models/

[3]: https://www.academia.edu/39366860/Narrative_Theory_for_Complexity_Scientists

[4]: https://academic.oup.com/dsh/article/36/2/322/5856850

[5]: https://www.researchgate.net/publication/232236967_A_tutorial_introduction_to_adaptive_fractal_analysis

[6]: https://www.intechopen.com/chapters/64463

[7]: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0085787

[8]: https://www.youtube.com/watch?v=blehVIDyuXk

[9]: https://www.youtube.com/watch?v=0cf-qdZ7GbA&list=PLSH_xM-KC3Zv-79sVZTTj-YA6IAqh8qeQ

[10]: https://dramatica.com/theory/book
