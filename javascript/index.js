function Person(name, age) {
    this.name = name;
    this.age = age;
  }
  
  Person.prototype.sayHello = function() {
    console.log("Hello, I'm " + this.name);
  };
  
  function Student(name, age, grade) {
    Person.call(this, name, age);
    this.grade = grade;
  }
  
  var student = new Student("Tom", 18, 3);
  
  student.sayHello()