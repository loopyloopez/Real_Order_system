import express from "express"
import axios from "axios"
import bodyParser from "body-parser";
const port = 8000;

const app = express();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.json());


app.post("/new",(req,res)=>{

    res.send("thank you");
    const content = req.body["name"] + "\n" +req.body["email"] + "\n" + req.body["orderDetails"] + "\n" + req.body["totalPrice"] + "\n";
    console.log(content);
    console.log("ordered received");
    axios.post('http://192.168.1.200:3000/neww', {
        firstName: req.body["name"],
        email: req.body["email"], OrderDetails:req.body["orderDetails"], totalPrice:req.body["totalPrice"]
      })
      .then(function (response) {
        console.log("sent");
      })
      .catch(function (error) {
        console.log(error);
      });
    console.log("process complete");



})

app.listen(port,'0.0.0.0',()=>{
    console.log("lestening on port 8000");
})