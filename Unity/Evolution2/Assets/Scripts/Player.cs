using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player : MonoBehaviour
{
    public bool leftThigh;
    public bool leftThighEx;
    public bool rightThigh;
    public bool rightThighEx;
    public bool leftLeg;
    public bool leftLegEx;
    public bool rightLeg;
    public bool rightLegEx;

    public Muscle[] bodyMuscles;
    public Muscle[] leftThighMuscles;
    public Muscle[] rightThighMuscles;

    GameObject barrier;
    public GameObject body;

    public bool dead = false;
    public float distance = 0f;

    // Start is called before the first frame update
//---------------------------------------------------------------------
    void Start()
    {
        barrier = GameObject.Find("Barrier");
    }


    // Update is called once per frame
    void Update()
    {
        if (dead && body == null){
            dead = false;
        }
        else if(dead){
            return;
        }
        

        //rightThigh= true;

        checkMuscles();
        if(body != null){
            if (barrier.transform.position.x >= body.transform.position.x){
                dead = true;
                distance = body.transform.position.x;
                //Debug.Log(distance + " meters");
            } 
        }
    }
    public float fitness(){
        return distance;
    }
    void checkMuscles(){
        if(rightThigh){
            bodyMuscles[0].contract = true;
        }
        else{
            bodyMuscles[0].contract = false;
        }

        if(leftThigh){
            bodyMuscles[1].contract = true;
        }
        else{
            bodyMuscles[1].contract = false;
        }

        if(rightThighEx){
            bodyMuscles[2].contract = true;
        }
        else{
            bodyMuscles[2].contract = false;
        }

        if(leftThighEx){
            bodyMuscles[3].contract = true;
        }
        else{
            bodyMuscles[3].contract = false;
        }

        if(leftLeg){
            leftThighMuscles[0].contract = true;
        }
        else{
            leftThighMuscles[0].contract = false;
        }

        if(leftLegEx){
            leftThighMuscles[1].contract = true;
        }
        else{
            leftThighMuscles[1].contract = false;
        }

        if(rightLeg){
            rightThighMuscles[0].contract = true;
        }
        else{
            rightThighMuscles[0].contract = false;
        }

        if(rightLegEx){
            rightThighMuscles[1].contract = true;
        }
        else{
            rightThighMuscles[1].contract = false;
        }
    }
//---------------------------------------------------------------------
}