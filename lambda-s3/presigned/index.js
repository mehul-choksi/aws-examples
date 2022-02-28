const aws = require('aws-sdk')

const s3 = new aws.S3();

exports.handler = async (event) => {
	// Get a presigned url for s3 bucket with put operation
	// Return url is successful, else return error

	const bucketName = 's3-presigned-url-mehul'
	const key = 'sample_file.json'
	const expirationInSeconds = 60 * 5;
	let url = '';
	try{
		url = s3.getSignedUrl('putObject', {
			Bucket: bucketName,
			Key: key,
			Expires: expirationInSeconds
		})

		console.log('Url is ' + url);
	}
	catch(err){
		return {
		    'statusCode': 400,
		    'body': err
		}
	}
	
	return {
		'statusCode' : 200,
		'body' : url
	}
}
