import express from "express"
import axios from "axios"
import bodyParser from "body-parser";
const port = 8000;
app.use(bodyParser.urlencoded({ extended: true }));

const app = express();




app.post("/new",(req,res)=>{

    res.send("thank you");
    const content = req.body["name"] + "\n" +req.body["email"] + "\n" + req.body["orderDetails"] + "\n" + req.body["totalPrice"] + "\n";
    console.log(content);



})

app.listen(port,()=>{
    console.log("lestening on port 8000");
})