import streamlit as st
from module import *

st.set_page_config(layout="wide")

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

st.markdown("<h1 style='text-align: center; color: black;'>Beaune et Pinot Noir</h1>",
            unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; color: black;'>Se positionner sur le marché américain du vin bourguignon </h3>",
            unsafe_allow_html=True)

st.markdown("<h2 style='text-align: left; color: black;'>Rappel du contexte et de la problématique</h2>",
            unsafe_allow_html=True)

"""
Revendeur de vins de la région de Bourgogne, vous nous avez demandé une analyse vous permettant de mieux appréhender le marché américain et vous positionner dedans.

Spécifiquement, vous désirez :
* d'une part une analyse générale du marché du vin et plus particulièrement de ce qui est pertinent relativement à votre offre ;
* d'autre part le moyen d'évaluer les prix auxquels proposer vos bouteilles."""

st.markdown("<h2 style='text-align: left; color: black;'>Méthodologie, outils et langages utilisés</h2>",
            unsafe_allow_html=True)

"""
Dans le contexte de cette première prise de contact, nous avons pris la décision de tout produire directement en lignes de code, sous le langage Python, nous offrant la plus grande flexibilité et adaptabilité. Nous travaillons les données aux moyens de la bibliothèque pandas, nous utilisons matplotlib, parfois seaborn, pour les visualisations, et ce site lui-même est produit avec la bibliothèque streamlit.

En ce qui concerne l'analyse des données, ce que l'on vous propose doit être considéré comme un exemple de ce qui est possible. Notre collaboration peut s'arrêter là, ou bien continuer si vous souhaitez nous soumettre des questions plus précises auxquelles nous nous efforcerons de répondre.

En ce qui concerne la prédiction des prix, en revanche, sans qu'il soit parfait nous vous offrons un produit fini et fonctionnel. Néanmoins, là encore, si vous souhaitez poursuivre la collaboration, nous pourrons voir à améliorer nos métriques à la suite d'une discussion avec vous sur la dimension métier.

L'ensemble du travail présenté est visible dans un notebook hébergé par Google Colab :

https://colab.research.google.com/drive/1Oqmh5u2YrbbkmxB9V40gUxaIv2mGd-_q?usp=sharing 

Nous vous en présentons ici des extraits à fins de clarté.

Pour voir le résultat final concernant la suggestion de prix, vous pouvez aller tout de suite consulter la dernière section, "Prédiction".
"""
st.markdown("<h2 style='text-align: left; color: black;'>Le Marché du Vin : analyse exploratoire</h2>",
            unsafe_allow_html=True)

"""
Notre approche, dans l'ensemble de cette analyse, a été de procéder selon trois niveaux :
* Le premier niveau considère le marché américain du vin dans son ensemble, tel que présenté dans le dataset fourni;
* Le second niveau considère deux parts substantielles de ce marché, à savoir d'un côté les Pinot Noir, conformément à votre demande, et de l'autre les vins de Bourgogne;
* Enfin, nous avons décidé de nous concentrer plus particulièrement sur les vins d'appellation Beaune, un bien plus petit ensemble (environ 160 bouteilles sur le dataset) mais qui représente l'essentiel de votre offre.
"""

st.markdown("<h3 style='text-align: left; color: black;'>Quelques métriques</h3>",
            unsafe_allow_html=True)

st.markdown("<h4 style='text-align: left; color: black;'>Les Américains et le Pinot Noir</h4>",
            unsafe_allow_html=True)

"Commençons par une vue d'ensemble du marché américain. Sans trop de surprise, les vins américains y sont largement dominants, mais la France arrive en bonne seconde place, suivie de près par l'Italie."

st.image("images\compte_vins_par_pays.png",
             #width=500,
             )

"En termes de cépage, les deux gagnants y sont le Pinot Noir et le Chardonnay. Bonne nouvelle : ce sont les deux que vous proposez. Votre offre semble devoir s'insérer adéquatement dans le paysage américain."

st.image("images\compte_vins_par_variete.png",
             #width=1000,
             )

"Si on se concentre sur le Pinot Noir, on remarque cependant que la production américaine y est encore plus largement dominante. Votre offre va donc vraisemblablement remplir une niche plus spécifique, celle des amateurs du terroir bourguignon."

st.image("images\pinot_per_country.png",
             #width=1000,
             )

st.markdown("<h4 style='text-align: left; color: black;'>Des prix qui penchent à droite</h4>",
            unsafe_allow_html=True)

"Nous ne vous apprenons rien en notant que l'offre oenologique est caractérisée par l'existence de bouteilles à des prix presque sans limite. Cela ne change pas, à cet égard, si l'on se concentre sur la région de Bourgogne ou sur le Pinot Noir. Ignorant ces valeurs, cependant, on obtient une distribution relativement régulière, qui continue de pencher à droite, de se caractériser par des bouteilles chères et rares."

st.image("images\distribution_prix.png",
             #width=1000,
             )

"Les choses changent, relativement, si l'on concentre sur les vins de Beaune. Continuant de pencher à droite, l'ensemble est dépourvu de valeurs aberrantes, et montre un territoire à prix élevés mais assez réguliers, avec une moyenne à 57\$ et une médiane à 53\$."

st.image("images\\beaune_distribution_prix.png",
             #width=1000,
             )

st.markdown("<h4 style='text-align: left; color: black;'>Un terroir apprécié</h4>",
            unsafe_allow_html=True)

"Dans l'ensemble du dataset, les notes sont réparties de façon à peu près normale, autour d'un score de 88."

st.image("images\distribution_notes.png",
             #width=1000,
             )

"Dans ce contexte, tant le Pinot Noir que les vins de Bourgogne sont déjà gagnants, avec une moyenne d'environ deux points supplémentaires."

col1, col2 = st.columns(2)
with col1:
    st.image("images\pinot_distribution_notes.png",
            caption="Les Notes du Pinot",
             #width=1000,
             )
with col2:
    st.image("images\\bourgogne_distribution_notes.png",
            caption="Les Notes Bourguignonnes",
             #width=1000,
             )

"Mais ce sont les vins de Beaune qui offrent un résultat spectaculaire, n'étant presque jamais dans le bas du panier et affichant une moyenne au delà de 91 et une forte présence dans la fourchette 91-95."

st.image("images\\beaune_distribution_notes.png",
             #width=1000,
             )

st.markdown("<h4 style='text-align: left; color: black;'>D'où viennent les prix ?</h4>",
            unsafe_allow_html=True)

"""
Pour le dire simplement, à cause de la variété des contextes de production au niveau international (et même localement), ni l'âge du vin ni son score ne sont dans l'ensemble de très bons prédicteurs de son prix, même si dans l'ensemble les vieilles bouteilles en vente tendent à être plus chères, ainsi que les bouteilles mieux notées. Dans le territoire de Beaune, on remarque une particularité, qui est que le millésime tend à être plutôt bien (négativement) corrélé avec à la fois la note et le prix ! Les vieux vins du terroir sont, dans l'ensemble, des références solides.
"""

col1, col2, col3 = st.columns(3)
with col1:
    st.image("images\heatmap.png",
            caption="Corrélation Viticoles",
             #width=1000,
             )
with col2:
    st.image("images\\bourgogne_heatmap.png",
            caption="Corrélations Bourguignonnes",
             #width=1000,
             )

with col3:
    st.image("images\\beaune_heatmap.png",
            caption="Corrélations Beaunoises",
             #width=1000,
             )

st.image("images\\beaune_price_per_year.png",
    caption="Prix et Années à Beaune",
             #width=1000,
             )

st.markdown("<h4 style='text-align: left; color: black;'>Les vendeurs</h4>",
            unsafe_allow_html=True)

"""Enfin, nous vous proposons (à voir plus complètement dans le notebook), les informations sur le marché sous la forme synthétique de tableaux des métriques par vendeurs, avec ici des extraits : 
* Concernant d'abord les vendeurs de vins de Bourgogne..."""

bourgogne_sellers

"""
* Et plus spécifiquement de Beaune.
"""

beaune_sellers


st.markdown("<h3 style='text-align: left; color: black;'>Que disent-ils ?</h3>",
            unsafe_allow_html=True)

"""
Nous vous proposons également de brèves visualisations de ce qui se dit sur le vin, fondées sur un nettoyage des commentaires critiques présents dans la database.

Que disent les gens, parlant du vin ? Si l'on prend une visualisation brute des mots employés, l'on tombe sur les caractéristiques les plus générales et attendues, tandis qu'une recherche textuelle plus attentive aux combinaisons de mots va révéler une obsession particulière : les fruits rouges.
"""
col1, col2 = st.columns(2)
with col1:
    st.image("images\words\wordfreq.png",
             #width=1000,
             )
with col2:
    st.image("images\words\wordcloud.png",
             #width=1000,
             )

"""
Du côté du Pinot les critiques remarquent de façon prédominante la cerise, et s'y attendent. Généralement, et naturellement, ils sont sensibles à la dimension fruitée du cépage, et à son tannin. Du côté de la Bourgogne, le fruit frappe encore, mais aussi très nettement l'acidité, ainsi que la richesse et le caractère de la région.
"""

col1, col2 = st.columns(2)
with col1:
    st.image("images\words\pinot_wordfreq.png",
            caption="Les Mots du Pinot",
             #width=1000,
             )
with col2:
    st.image("images\words\\bourgogne_wordcloud.png",
            caption="Les Mots de la Bourgogne",
             #width=1000,
             )

"""
Concentrons-nous finalement sur Beaune. Là, nous rencontrons toutefois une limitation, qui est que tous les vins du terroir sont commentés par la même personne, sauf erreur : Roger Voss. Les analyses lexicales sont donc nécessairement dépendantes de ses idiosyncrasies de langage. Nous remarquons toutefois de nouveau l'importance du tannin, du fruit et de l'acidité, ainsi que la présence discrète du bois et de la saveur fumée.
"""

st.image("images\words\\beaune_wordcloud.png",
            caption="Les Mots de Beaune",
             #width=1000,
             )


"Notez enfin que ces appréciations impressionnistes peuvent être complétées par des études plus prosaïque de fréquence, dont nous donnons ici un extrait pour la Bourgogne."

st.image("images\words\\bourgogne_words.png",
             #width=1000,
             )

"""
Du fait de la manière dont le code est rédigé, il sera aisé, par la suite, de produire l'ensemble des visualisations ici présentées, et d'autres, pour un sous-ensemble différent du dataset.
"""

st.markdown("<h2 style='text-align: left; color: black;'>Prédiction</h2>",
            unsafe_allow_html=True)

"""
Voici, sans plus tarder, le résultat auquel parvient notre modèle de prédiction et les prix qu'il suggère pour votre catalogue :
"""

df_croix_predicted[["title","millesime","variety","region_1","predicted_price"]]

"""
Le principe de notre prédiction a été le suivant : face au peu de fiabilité de l'age et du score pour la détermination du prix, nous avons tout de suite envisagé d'utiliser les caractéristiques régionales et de cépage comme des prédicteurs. Pour cela, il faut parvenir à les transformer en chiffres utiles, ce que nous avons fait en remplaçant ces valeurs (pays, région, cépage, etc.) par la moyenne du prix des vins ayant cette valeur une fois écartés les valeurs aberrantes que l'on sait si présentes dans le domaine du vin.

Ainsi, par exemple, Beaune se voit remplacer par 48.6055.

Le fait d'écarter les valeurs aberrantes fait déjà monter le score R2 de la prédiction jusqu'aux alentours de 0.6 (pensez 60% de fiabilité). Grâce à la numérisation des valeurs catégoriques on arrive à un score probablement d'environ .86 ! Il faut néanmoins prendre ce chiffre avec des pincettes, comme nous allons le voir.

Auparavant, un mot sur l'algorithme lui-même. Il s'agit, généralement parlant, d'un algorithme de "régression", c'est-à-dire qu'il détermine la manière optimale de multiplier chacune des valeurs données en entrée pour obtenir en moyenne un résultat aussi proche que possible de la vérité.

Le modèle ici utilisé s'appelle "Random Forest Regressor", et il consiste à appliquer et tester de façon intelligente des calculs de type "arbre", qui séparent successivement en deux le dataset selon le critère le plus pertinent à chaque étape.

Nous vous fournissons, non seulement une prédiction sur l'échantillon que vous nous fournissez, mais aussi une fonction capable de générer en une seconde une prédiction sur n'importe quel dataset formaté de la même manière.

A la fois les bugs et les variations de performance possibles vont dépendre des colonnes non remplies dans les dataset fournis, et du degré auquel les vins proposés ressemblent aux vins déjà existant sur le marché. La prédiction est à son comble quand elle a des valeurs moyenne non seulement pour la région, mais pour le domaine. Votre domaine étant nouveau dans la database, il n'apparait jamais, et pour certaines des bouteilles, qui ne sont pas marquées comme de Beaune, la database ne possédait pas non plus assez d'information pour établir une valeur moyenne pour leur terroir : notre code va substituer la moyenne de la région à celle du terroir, et cette dernière à celle du domaine, le cas échéant, la prédiction restant aussi précise que possible.
"""