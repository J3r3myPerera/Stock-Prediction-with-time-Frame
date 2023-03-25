const firebaseConfig = {
    apiKey: "AIzaSyD5quApqkViDlzTqO4sJry9-DqdxUityZo",
    authDomain: "the-predictor-c0c13.firebaseapp.com",
    databaseURL: "https://the-predictor-c0c13-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "the-predictor-c0c13",
    storageBucket: "the-predictor-c0c13.appspot.com",
    messagingSenderId: "136843663662",
    appId: "1:136843663662:web:d91d160d21a413b59482bf",
    measurementId: "G-Q3C4Q4XY4V"
  };


//Initialize firebase 
firebase.initializeApp(firebaseConfig);

//Reference for the database
var contactFormDB = firebase.database().ref('contactForm');

document.getElementById('contactForm').addEventListener("submit",submitForm);

function submitForm(e){
    e.preventDefault();

    var name=getElementVal('persondetails');
    var email=getElementVal('emaildetails');
    var password=getElementVal('passswordid');

    console.log(name,email,password);
}

const getElementVal=(id)=>{
    return document.getElementById(id).value;
}