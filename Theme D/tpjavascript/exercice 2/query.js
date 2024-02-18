var query = document.querySelector("nav ul li");
console.log("Affichage de query");
console.log(query);

var queryAll_1 = document.querySelectorAll(".menu li");
console.log("Affichage de queryAll_1");
console.log(queryAll_1);

console.log("Affichage de chaque éléments de queryAll_1 par appels successifs")
console.log(queryAll_1[0]);
console.log(queryAll_1[1]);
console.log(queryAll_1[2]);

var queryAll_2 = document.querySelectorAll("nav ul li");
console.log("Affichage de queryAll_2");
console.log(queryAll_2);

console.log('Affichage de chaque éléments de queryAll_1 avec une boucle pour : ');


for (let index = 0; index < queryAll_2.length; index++) {
    const element = queryAll_2[index];
    console.log(element);
    }

var important = document.querySelector("#important");
/* Affichage de l'élément sélectionné ayant l'ID important. */
alert(important);
/* Affichage du contenu du paragraphe ayant l'ID important. */

alert(important.innerHTML);

/* Modification du paragraphe */
important.innerHTML = " Voici une citation d'Alan Turing : <q> Les tentatives de création de machines pensantesnous seront d'une grande aide pour découvrir comment nous pensons nous-mêmes. </q>";