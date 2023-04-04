// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
var firebaseConfig = {
  apiKey: "AIzaSyBPOC9GeRJBrBnY0-bE0I4pWeNcmU8t6VY",
  authDomain: "the-hell-c1059.firebaseapp.com",
  projectId: "the-hell-c1059",
  storageBucket: "the-hell-c1059.appspot.com",
  messagingSenderId: "558470682546",
  appId: "1:558470682546:web:b3912bce9e20093cdfb6ab",
  measurementId: "G-VPBKD8M0QS"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

//Initialize Firebase
const auth=firebase.auth()
const database=firebase.database()

//Set up register
function register(){
  username=document.getElementById('username').value
  email=document.getElementById('email').value
  password=document.getElementById('passsword').value

  if(validate_email(email)==false || validate_password(passsword)==false){
    alert('Email or Password out of line!! ')
  }

  if(validate_field(username)==false){
    alert('Fields are out of lines')
  }

  auth.createUserwithEmailandPassword(email,password)
  .then(function(){

    var user=auth.currentUser
    var database_ref=database.ref()

    var user_data={
      email : email,
      username : username,
      last_login : Date.now()
    }
    database_ref=child('users/' + use.uid).set(user_data)
    
    alert('user created')

  })
  .catch(function(error){
    var error_code=error.code 
    var error_message=error.message 

    alert(error_message)
  })
}

function validate_email(email){
  expression=/^[^@]+@\w+(\.\w+)+\w$/;
  if(expression.test(email)){
    return true;
  }else{
    return false;
  }
}

function validate_password(passsword){
  if(passswordid < 6){
    return false
  }else{
    return true;
  }
}

function validate_field(username){
  if(field==null){
    return false;
  }
  if(field.length <=0){
    return false;
  }else{
    return true;
  }
}