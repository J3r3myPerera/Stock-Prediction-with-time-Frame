// let reviews = [];
// let reviewTextBox;
let reviewArray = [
  "This is a good prediction",
  "Its very easy to understand",
  "Very timely",
];
let nameArray = ["Dinuka", "Nadil", "Lohim"];

function addReview() {
  // var count = 0;

  // let name_value = document.getElementById("name").value;
  // let review_value = document.getElementById("review").value;

  // nameArray.push(name_value);
  // reviewArray.push(review_value);
  // name_value.value = "";
  // review_value.value = "";

  // Create a new review object with a unique ID
  // let newReview = {
  //   id: Date.now(),
  //   name: name,
  //   review: review,
  // };

  // // Add the new review to the array of reviews
  // reviews.push(newReview);

  // Clear the input fields
  // document.getElementById("name").value = "";
  // document.getElementById("review").value = "";

  // Show the review textbox
  // if (!reviewTextBox) {
  //   reviewTextBox = document.createElement("textarea");
  //   reviewTextBox.id = "review-textbox";
  //   reviewTextBox.classList.add("review-textbox");
  //   document.getElementById("reviews-container").appendChild(reviewTextBox);
  // }
  // reviewTextBox.value = review;

  document.getElementById("mytextBox1").value = nameArray[0];
  document.getElementById("myTextBox2").value = reviewArray[0];

  document.getElementById("mytextBox2").value = nameArray[1];
  document.getElementById("myTextBox3").value = reviewArray[1];

  document.getElementById("mytextBox").value = nameArray[2];
  document.getElementById("myTextBox4").value = reviewArray[2];

  console.log(nameArray);
  console.log(reviewArray);
}
