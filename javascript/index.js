function Animal(name) {
  this.name = name || 'Animal';
  this.sleep = function() {
    console.log(this.name + ' is sleeping')
  } 
};

Animal.prototype.eat = function (food) {
  console.log(this.name + " is eating " + food);
};



Animal.prototype.eat.call({name:'anqi',food: 'banana'});