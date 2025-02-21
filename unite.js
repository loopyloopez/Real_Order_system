import express from "express"
import axios from "axios"
import bodyParser from "body-parser";
const port = 8000;

const app = express();

app.use(bodyParser.urlencoded({ extended: true }));



app.post("/new",(req,res)=>{

    res.send("thank you");
    const content = req.body["name"] + "\n" +req.body["email"] + "\n" + req.body["orderDetails"] + "\n" + req.body["totalPrice"] + "\n";
    console.log(content);
    console.log("ordered received");
    axios.post('/new', {
        firstName: req.body["name"],
        email: req.body["email"], OrderDetails:req.body["orderDetails"], totalPrice:req.body["totalPrice"]
      })
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });



})

app.listen(port,()=>{
    console.log("lestening on port 8000");
})