import axios from "axios"


axios.post('http://192.168.1.229:3000/neww', {
        firstName: "name",
        email: "emi", OrderDetails:"ddeets", totalPrice:"total"
      })
      .then(function (response) {
        console.log("sent");
      })
      .catch(function (error) {
        console.log(error);
      });
    console.log("process complete");