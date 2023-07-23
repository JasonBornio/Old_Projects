using System.Collections;
using System.Collections.Generic;
using UnityEngine;

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

        List<Brain> survivors = new List<Brain>();
        int survivorCount = Mathf.RoundToInt(population.Count * (cutoff/100));

        for (int i =0; i <survivorCount; i++ ){
            survivors.Add(getFittest());
        }
        Debug.Log("ok");

        for (int i = 0; i < populationSize; i++){
            Destroy(population[i].gameObject);
            Destroy(playerPopluation[i].gameObject);
        }
        

        Debug.Log("ok2");

        population.Clear();
        playerPopluation.Clear();
        int counter  = 0;
        network parent = new network(7,8,2,10,true);

        Debug.Log("ok3");

            for(int i = 0; i < populationSize; i++){
                GameObject go = Instantiate(bot);
                go.GetComponent<Brain>().intiNetwork(new network(),learningrate);
                go.GetComponent<Brain>().net.copy(survivors[0].net);
                if(i > 2){
                    go.GetComponent<Brain>().net.evolve(i);
                }
                population.Add(go.GetComponent<Brain>());
                playerPopluation.Add(go.GetComponent<Player>());

                connectBody(go);
                counter += 1;
                if(counter == survivorCount){
                    counter = 0;
                }
            }
            
        
        Debug.Log("ok4");
        for(int i = 0; i < survivors.Count; i++){
            Destroy(survivors[i].gameObject);
        }
        
        reset();
        barrier.GetComponent<Barrier>().move = true;
    
    }

    private Brain getFittest(){
        Brain survivor = new Brain();
        GameObject go = Instantiate(bot);
        go.GetComponent<Brain>().intiNetwork(new network(),learningrate);
        float fitness = 0f;
        float max = -1000f;
        int index= 0;
        for(int i = 0; i<population.Count; i++){
            fitness = playerPopluation[i].fitness();
            if(fitness > max){
                max = fitness;
                index = i;
            }
        }
        //playerPopluation.Remove(playerPopluation[index]);
        go.GetComponent<Brain>().net.copy(population[index].net);
        //population.Remove(survivor);
        return go.GetComponent<Brain>();
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
