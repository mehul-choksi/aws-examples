const AWS = require('aws-sdk');
const S3 = new AWS.S3();

/**
 * Lambda implementation which will be used in widget service
 * Bucket name will be passed during creation of lambda handler in widget service using cdk
 */

const bucketName = process.env.BUCKET;

exports.main = async (event, context) => {
    try{
        let methodType = event.httpMethod;
        if(methodType === 'GET'){
            if(event.path === '/'){
                const data = await S3.listObjectsV2({Bucket : bucketName}).promise();
                const body = {
                    widgets : data.Contents.map(e => e.key)
                };
                return {
                    statusCode : 200,
                    headers : {},
                    body : JSON.stringify(body) + "****** bucketName " + JSON.stringify(bucketName)
                }
            }
        }
        // Other httpMethod types are not implemented, so return an error
        return {
            statusCode : 400,
            headers : {},
            body : "We only accept get http method with / path " + " **** bucketName " + JSON.stringify(bucketName)
        }
    }
    catch(error){
        let body = error.stack || JSON.stringify(error,null,2);
        return {
            statusCode : 400,
            headers : {},
            body : JSON.stringify(body) + "***** bucketName " + JSON.stringify(bucketName)
        }
    }
}