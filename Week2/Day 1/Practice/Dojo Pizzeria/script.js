
//function pizza
function pizza(crustType, sauceType, cheeses, toppings) {
    var pizza = {};
    pizza.crustType = crustType;
    pizza.sauceType = sauceType;
    pizza.cheeses = cheeses;
    pizza.toppings = toppings;
    return pizza;
}
//pizza 1
var pizza1 = pizza("deep dish", "traditional", ["mozzarella"], ["pepperoni", "sausage"]);
console.log("pizza 1 :",pizza1);
//pizza 2
var pizza2= pizza("hand tossed","marinara",["mozzarella","feta"],["mushrooms","olives","onions"]);
console.log("pizza 2 : ", pizza2);
//pizza 3
var pizza3= pizza("Cracker Crust","Buffalo Sauce",["Gouda","Gruyere"],["Sausage","Kale","Pepperoni"]);
console.log("pizza 3 : ", pizza3);
//pizza 4
var pizza4= pizza("Thin Crust","Hummus","Cheddar Cheese","pepperoni");
console.log("pizza 4 : ", pizza4);


//function randomPizza

var crustType =["deep dish","hand tossed","Cracker Crust","Thin Crust"];
var sauceType =["traditional","marinara","Buffalo Sauce","Hummus"];
var cheeses =["mozzarella","feta","Gouda","Gruyere"];
var toppings =["pepperoni","sausage","mushrooms","olives"];
function random(array){
    var random =Math.ceil((array.length-1)*Math.random());
    return array[random];

}
function randomPizza(){

    var pizza = {};
    pizza.crustType = random(crustType);
    pizza.sauceType = random(sauceType);
    pizza.cheeses = random(cheeses);
    pizza.toppings = random(toppings);
    return pizza;  
}
console.log(randomPizza());