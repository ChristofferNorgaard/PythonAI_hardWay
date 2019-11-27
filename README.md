# Projekt za informatiko November - December 2019
### Povzetek - Abstract
Namen tega projekta je narediti AI za prepoznavanje napisanih številk iz baze podatkov 
[THE MNIST DATABASE of handwritten digits](http://yann.lecun.com/exdb/mnist/).
Program bo napisan v Python-u, vendar pa **ne bo** uporabljal knjižnic, ki so namenjene ustvarjanju AI-jov. Tako bodo vsi deli implementirani v kodi sami. Končni produkt bo AI, ki bo znal za dano napisano številko povedati za katero gre z več ko 50% verijetnostjo. (Cilj tega projekti ni postavljen preveč visoko z razlogom). 

## Postopek programiranja
### Podatki

[THE MNIST DATABASE of handwritten digits](http://yann.lecun.com/exdb/mnist/), ki se bo v nadaljevanju imenovala **MN DATABASE** je sestavljena iz dveh skupin setov, eden za učenje AI, drugi pa za testiranje. Oba imata več kot 30 000 primerov, plod dela 250 različnih avtorjev. 

Set je v MN DATABASE sestavljen iz dveh podatkov, eden izmed njih je slika rezolucije 28x28 pikslov, drugi pa števka, ki je bila zapisana. 
![alt text](https://3qeqpr26caki16dnhd19sv6by6v-wpengine.netdna-ssl.com/wp-content/uploads/2016/05/Examples-from-the-MNIST-dataset.png)

\*Url: [https://machinelearningmastery.com/handwritten-digit-recognition-using-convolutional-neural-networks-python-keras/](https://machinelearningmastery.com/handwritten-digit-recognition-using-convolutional-neural-networks-python-keras/)*

### Načrt programiranja

1. Teorija

Ai bo zahteval precej poglablanja v matematiko in ostalega teoretičnega znanja. Nekaj tega predznanja že imam, kljub temu pa pričakujem, da bom tukaj preživel največ časa. Vse te informacije bodo zbrane v sekciji UVOD.
2. Osnovna koda Ai

Osnovno Ai drevo in implementacija *Neuronov, Povezav, računanja napake (cost function), uvoza podatkov...* 

Ai bo sprogramiran v obliki dva sloja po 16 neuronov in 10 iztopnih neuronov. Vsak pixel je svoj vstopni neuron.
3. Test na manjših količinah podatkov

Najprej bom Ai testiral na pribljižno 10ih setih in te podatke beležil. Tukaj nastopi tudi razhroščevanje kode.
4. Učenje AI-ja

Ai se bo učil na skupini setov SD-1, tokrat z vsemi podatki. Test uspešnosti bo narejen na skupini SD-2.
5. DODATEK: Vizualizacija AI-ja

Drevo in povezave ter delovanje Ai-ja bom poizkušal tudi grafično pokazati.
