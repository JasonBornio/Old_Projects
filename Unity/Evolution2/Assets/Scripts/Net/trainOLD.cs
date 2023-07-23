using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class trainOLD : MonoBehaviour
{
/*
    public GameObject bot;
    public GameObject bestBot;
    private GameObject barrier;
    List<GameObject> botPopulation = new List<GameObject>();
    List<Brain> population = new List<Brain>();
    List<Player> playerPopluation = new List<Player>();
    public int populationSize = 5;
    public float maxDistance = -10f;
    public List<float> distances = new List<float>();
    public float thres = 0.75f;
    public float learningrate = 0.1f;
    private int noOfgo = 6;
    public bool best = false;
    public float times = 1f;

    void initialise(){
        for(int i = 0; i < populationSize; i++){
            if(i == 0){
                
                bestBot = Instantiate(bot);
                bestBot.GetComponent<Brain>().intiNetwork(new network(7,8,2,10,true),learningrate);
                best = true;
                population.Add(bestBot.GetComponent<Brain>());
                playerPopluation.Add(bestBot.GetComponent<Player>());

                connectBody(bestBot);
            }
            else{

                GameObject go = Instantiate(bot);
                go.GetComponent<Brain>().intiNetwork(new network(7,8,2,10,true),learningrate);


                population.Add(go.GetComponent<Brain>());
                playerPopluation.Add(go.GetComponent<Player>());

                connectBody(go);


            }

            distances.Add(0f);
        }
        barrier.GetComponent<Barrier>().move = true;
    }

    void nextGeneration(){

        int index = 0;
        for(int i = 0; i < populationSize; i++){
            distances[i] = playerPopluation[i].distance;
            if(distances[i] > maxDistance){
            maxDistance = distances[i];
            index = i;
            }
        }

        Brain parent = population[index];
        List<Brain> survivors = new List<Brain>();
        //population.Clear();

        for (int i = 0; i < populationSize; i++){
            population[i].net.copy(parent.net);
            if(i != 0){
                population[i].net.evolve(0);
            }
            survivors.Add(population[i]);
        }

        for (int i = 0; i < populationSize; i++){
            Destroy(population[i].gameObject);
        }

        population.Clear();
        playerPopluation.Clear();
///////////////////////////////////////////////
        for(int i = 0; i < populationSize; i++){
            if(i == 0){
                
                bestBot = Instantiate(bot);
                bestBot.GetComponent<Brain>().intiNetwork(new network(7,8,2,10,false),learningrate);
                bestBot.GetComponent<Brain>().net.copy(survivors[i].net);
                best = true;
                population.Add(bestBot.GetComponent<Brain>());
                playerPopluation.Add(bestBot.GetComponent<Player>());

                connectBody(bestBot);
            }
            else{

                GameObject go = Instantiate(bot);
                go.GetComponent<Brain>().intiNetwork(new network(7,8,2,10,false),learningrate);
                go.GetComponent<Brain>().net.copy(survivors[i].net);


                population.Add(go.GetComponent<Brain>());
                playerPopluation.Add(go.GetComponent<Player>());

                connectBody(go);
            } 
            Debug.Log("IIIIIIII:" + i);
        }
        
        reset();
        barrier.GetComponent<Barrier>().move = true;
    }

    void connectBody(GameObject go){

            for(int i = 0; i < go.transform.childCount; i++){
                Transform t = go.transform.GetChild(i);
                t.gameObject.name = "Bot " + i.ToString();
                Debug.Log("child:" + t.name);
            }

            Brain brn = go.GetComponent<Brain>();
            Player ply = go.GetComponent<Player>();
            Transform tr = go.transform;

            brn.body = tr.GetChild(0).gameObject.GetComponent<Rigidbody2D>();
            brn.player = tr.GetComponent<Player>();
            brn.threshold = thres;
            brn.leftLegCollider = tr.GetChild(3).gameObject.GetComponent<groundCollider>();
            brn.rightLegCollider = tr.GetChild(4).gameObject.GetComponent<groundCollider>();
            brn.bodyCollider = tr.GetChild(0).gameObject.GetComponent<groundCollider>();

            ply.body = tr.GetChild(0).gameObject;
            ply.bodyMuscles = tr.GetChild(0).gameObject.GetComponents<Muscle>();
            ply.leftThighMuscles = tr.GetChild(2).gameObject.GetComponents<Muscle>();
            ply.rightThighMuscles = tr.GetChild(1).gameObject.GetComponents<Muscle>();
            ply.dead = false;
    }

    public bool done(){
        if (population.Count <= 0){
            return false;
        }
        for(int i = 0; i < populationSize; i++){
            if(population[i].hasDied == false){
                Debug.Log("false");
                return false;
            }
        }
        Debug.Log("true");
        return true;
    }

    void reset(){

        barrier.GetComponent<Barrier>().move = false;
        barrier.transform.position = new Vector3(-100f, barrier.transform.position.y, barrier.transform.position.z);
        Debug.Log("RESET");
        for(int i = 0; i < populationSize; i++){
            //botPopulation[i].transform.position = new Vector3(0,0,0);
            //botPopulation[i].transform.rotation = Quaternion.identity;
            playerPopluation[i].dead = false;
            population[i].hasDied = false;
        }

    }

    void spawn(){

    }

    void Start()
    {
        barrier = GameObject.Find("Barrier");
        Physics2D.IgnoreLayerCollision(6, 6);
        initialise();
        
    }

    void Update()
    {
        if(done()){
            nextGeneration();
        }
        
        Time.timeScale = times;
    }

    /*
        newBrain.body = trans.Find("body").gameObject.GetComponent<Rigidbody2D>();
        newBrain.player = ListOfBots[0].GetComponent<Player>();
        newBrain.threshold = thres;
        newBrain.leftLegCollider = trans.Find("LeftLeg").gameObject.GetComponent<groundCollider>();
        newBrain.rightLegCollider = trans.Find("RightLeg").gameObject.GetComponent<groundCollider>();
        newBrain.bodyCollider = trans.Find("body").gameObject.GetComponent<groundCollider>();

        play.body = trans.Find("body").gameObject;
        play.bodyMuscles = trans.Find("body").gameObject.GetComponents<Muscle>();
        play.leftThighMuscles = trans.Find("LeftThigh").gameObject.GetComponents<Muscle>();
        play.rightThighMuscles = trans.Find("RightThigh").gameObject.GetComponents<Muscle>();
        play.dead = false;
        play.reSetBarrier();
   */ 
}
 /*
 public class train : MonoBehaviour
{

    public GameObject bot;
    public GameObject bestBot;
    private GameObject barrier;
    List<GameObject> botPopulation = new List<GameObject>();
    List<Brain> population = new List<Brain>();
    List<Player> playerPopluation = new List<Player>();
    public int populationSize = 5;
    public float maxDistance = -10f;
    public List<float> distances = new List<float>();
    public float thres = 0.75f;
    public float learningrate = 0.1f;
    private int noOfgo = 6;
    public bool best = false;
    public float times = 1f;
    public int cutoff = 50;

    void initialise(){
        for(int i = 0; i < populationSize; i++){
            //if(i == 0){
                
            //    bestBot = Instantiate(bot);
            //    bestBot.GetComponent<Brain>().intiNetwork(new network(7,8,2,10,true),learningrate);
            //    best = true;
            //    population.Add(bestBot.GetComponent<Brain>());
            //    playerPopluation.Add(bestBot.GetComponent<Player>());

            //    connectBody(bestBot);
            //}
            //else{

                GameObject go = Instantiate(bot);
                go.GetComponent<Brain>().intiNetwork(new network(7,8,2,10,true),learningrate);


                population.Add(go.GetComponent<Brain>());
                playerPopluation.Add(go.GetComponent<Player>());

                connectBody(go);


            //}

            distances.Add(0f);
        }
        barrier.GetComponent<Barrier>().move = true;
    }

    void nextGeneration(){

        reset();
        List<Brain> survivors = new List<Brain>();
        int survivorCount = Mathf.RoundToInt(population.Count * (cutoff/100));

        for (int i =0; i <survivorCount; i++ ){
            survivors.Add(getFittest());
        }

        for (int i = 0; i < populationSize; i++){
            Destroy(population[i].gameObject);
            Destroy(playerPopluation[i].gameObject);
        }

        population.Clear();
        playerPopluation.Clear();
        int counter  = 0;

        while (population.Count < populationSize){

            for(int i = 0; i < survivors.Count; i++){
                GameObject go = Instantiate(bot);
                go.GetComponent<Brain>().intiNetwork(new network(7,8,2,10,false),learningrate);
                go.GetComponent<Brain>().net.copy(survivors[i].net);
                //if(i < 2){
                //    Debug.Log("yo");
                //}
                population.Add(go.GetComponent<Brain>());
                playerPopluation.Add(go.GetComponent<Player>());

                connectBody(go);
                counter += 1;
                if(population.Count >= populationSize){
                    break;
                }
            }
        }

        for(int i = 0; i < survivors.Count; i++){
            Destroy(survivors[i].gameObject);
        }
        
        barrier.GetComponent<Barrier>().move = true;
    }

    private Brain getFittest(){
        Brain survivor = new Brain();
        float fitness = 0f;
        float max = 0f;
        int index= 0;
        for(int i = 0; i<population.Count; i++){
            fitness = playerPopluation[i].fitness();
            if(fitness > max){
                max = fitness;
                index = i;
            }
        }
        survivor = population[index];
        population.Remove(population[index]);
        playerPopluation.Remove(playerPopluation[index]);
        return survivor;
    }

    void connectBody(GameObject go){

            for(int i = 0; i < go.transform.childCount; i++){
                Transform t = go.transform.GetChild(i);
                t.gameObject.name = "Bot " + i.ToString();
                Debug.Log("child:" + t.name);
            }

            Brain brn = go.GetComponent<Brain>();
            Player ply = go.GetComponent<Player>();
            Transform tr = go.transform;

            brn.body = tr.GetChild(0).gameObject.GetComponent<Rigidbody2D>();
            brn.player = tr.GetComponent<Player>();
            brn.threshold = thres;
            brn.leftLegCollider = tr.GetChild(3).gameObject.GetComponent<groundCollider>();
            brn.rightLegCollider = tr.GetChild(4).gameObject.GetComponent<groundCollider>();
            brn.bodyCollider = tr.GetChild(0).gameObject.GetComponent<groundCollider>();

            ply.body = tr.GetChild(0).gameObject;
            ply.bodyMuscles = tr.GetChild(0).gameObject.GetComponents<Muscle>();
            ply.leftThighMuscles = tr.GetChild(2).gameObject.GetComponents<Muscle>();
            ply.rightThighMuscles = tr.GetChild(1).gameObject.GetComponents<Muscle>();
            ply.dead = false;
    }

    public bool done(){
        //if (population.Count <= 0){
        //    return false;
        //}
        for(int i = 0; i < populationSize; i++){
            if(population[i].hasDied == false){
                Debug.Log("false");
                return false;
            }
        }
        Debug.Log("true");
        return true;
    }

    void reset(){

        barrier.GetComponent<Barrier>().move = false;
        barrier.transform.position = new Vector3(-100f, barrier.transform.position.y, barrier.transform.position.z);
        Debug.Log("RESET");
        for(int i = 0; i < populationSize; i++){
            playerPopluation[i].dead = false;
            population[i].hasDied = false;
        }

    }

    void Start()
    {
        barrier = GameObject.Find("Barrier");
        Physics2D.IgnoreLayerCollision(6, 6);
        initialise();
        
    }

    void Update()
    {
        if(done()){
            nextGeneration();
        }
        
        Time.timeScale = times;
    }

}
*/