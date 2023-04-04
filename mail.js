// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.18.0/firebase-app.js";
import {
  getFirestore,
  setDoc,
  addDoc,
  doc,
} from "https://www.gstatic.com/firebasejs/9.18.0/firebase-firestore.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.18.0/firebase-analytics.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCcb4iVrKLSN3KVrX5k0xZWIIGlFMvyAhg",
  authDomain: "the-predictor-5d01e.firebaseapp.com",
  projectId: "the-predictor-5d01e",
  storageBucket: "the-predictor-5d01e.appspot.com",
  messagingSenderId: "816069505487",
  appId: "1:816069505487:web:156e75b66f71ac0c2962ba",
  measurementId: "G-N6RPTRH7W4",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

// Initialize Cloud Firestore and get a reference to the service
const db = getFirestore(app);

var name = document.getElementById("name").value;
var email = document.getElementById("emaildetails").value;
var password = document.getElementById("passswordid").value;
submitdata.addEventListener("click", (e) => {
  addDoc(doc(db, "users"), {
    name: "name",
    email: "email",
    password: "passsword",
  });
  alert("User Added!");
});

const auth = firebase.auth();
const userDetails = document.getElementById("userDetails");

const provider = new firebase.auth.GoogleAuthProvider();

signInBtn.onclick = () => auth.signInWithPopup(provider);
