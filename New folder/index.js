"use strict"

const express = require("express");
const cors = require("cors");
const helmet = require("helmet");
const aws = require("aws-sdk");

const app = express();
app.use(helmet());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
const s3 = new aws.S3({ apiVersion: "2023-08-01" });

const handler = function (event, text, callback) {
    //console.log('Received event:', JSON.stringify(event, null, 2));

    // Get the object from the event and show its content type
    const bucket = event.Records[0].s3.bucket.name;
    const key = decodeURIComponent(event.Records[0].s3.object.key.replace(/\+/g, ' '));
    const params = {
        Bucket: bucket,
        Key: key
    }
    s3.getObject(params, (err, data) => {
        if (err) {
            console.log(err);
            const message = `Error getting object ${key} from bucket ${bucket}. Make sure they exist and your bucket is in the same region as this function.`;
            console.log(message);
            callback(message);
        } else {
            console.log('Content Type: ', data.ContentType);
            callback(null, data.ContentType);
        }
    })
}

handler()

app.listen(3000, () => console.log("Server started on port 3000"));