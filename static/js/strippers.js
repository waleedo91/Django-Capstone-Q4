const originalString = document.getElementById(review-text);
const strippedString = originalString.replace(/(<([^>]+)>)/gi, "");
console.log(strippedString);
