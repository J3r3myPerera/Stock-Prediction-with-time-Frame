const {MongoClient} = require('mongodb');

async function main(){

    const uri="mongodb+srv://<admin>:<admin>@cluster0.wlnwqve.mongodb.net/?retryWrites=true&w=majority";

    const client =new MongoClient(uri);

    try{
        await client.connect();

        await listDatabases(client);
    }catch (e){
        console.error(e);
    }finally{
        await client.close();
    }
}
    
main.catch(console.error);

async function listDatabases(client){
    const databaseslist = await client.db().admin.listDatabases();
    console.log("Databases : ");
    databaseslist.databaseslist.forEach(db=>{
        console.log('- ${db.name}')
    })
}