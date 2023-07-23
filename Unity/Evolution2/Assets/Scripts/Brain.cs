using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Reflection;
using UnityEditor;
public class Brain : MonoBehaviour
{
        /*
        1 - body on ground
        2 - left leg on ground
        3 - right leg on ground
        4 - rotation
        5 - x speed
        6 - y speed
        7 - angular velocity
        */
    public network net; 
    List<float> inputs = new List<float>();
    //public GameObject body
    public Rigidbody2D body;
    public Player player;
    public float threshold = 0.75f;
    public groundCollider leftLegCollider;
    public groundCollider rightLegCollider;
    public groundCollider bodyCollider;
    public bool hasDied = false;
    
    // Start is called before the first frame update

    void Start(){
        for(int i = 0; i < 7; i++){
            inputs.Add(0f);
        }
    }
    public void intiNetwork(network netw, float rate){
        net = netw;
        net.learningrate = rate;
    }

    private void checkOuputs(){
                
        if(net.outputs[0].getActivation() > threshold){
            player.leftThigh = true;
        }else{
            player.leftThigh = false;
        }

        if(net.outputs[1].getActivation() > threshold){
            player.leftThighEx = true;
        }else{
            player.leftThighEx = false;
        }

        if(net.outputs[2].getActivation() > threshold){
            player.rightThigh = true;
        }else{
            player.rightThigh = false;
        }

        if(net.outputs[3].getActivation() > threshold){
            player.rightThighEx = true;
        }else{
            player.rightThighEx = false;
        }

        if(net.outputs[4].getActivation() > threshold){
            player.leftLeg = true;
        }else{
            player.leftLeg = false;
        }

        if(net.outputs[5].getActivation() > threshold){
            player.leftLegEx = true;
        }else{
            player.leftLegEx = false;
        }

        if(net.outputs[6].getActivation() > threshold){
            player.rightLeg = true;
        }else{
            player.rightLeg = false;
        }

        if(net.outputs[7].getActivation() > threshold){
            player.rightLegEx = true;
        }else{
            player.rightLegEx = false;
        }

    }

    void getInputs(){

        if (bodyCollider.isGrounded){
            inputs[0] = 1f;
        } 
        else{ 
            inputs[0] = 0f;
        }
        if (leftLegCollider.isGrounded){
            inputs[1] = 1f;
        } 
        else{ 
            inputs[1] = 0f;
        }
        if (rightLegCollider.isGrounded){
            inputs[2] = 1f;
        } 
        else{ 
            inputs[2] = 0f;
        }
        inputs[3] = body.rotation;
        inputs[4] = body.velocity.x;
        inputs[5] = body.velocity.y;
        inputs[6] = body.angularVelocity/10f;

    }

    // Update is called once per frame
    void Update()
    {        

        if(hasDied){
            return;
        }

        getInputs();

        net.feedForward(inputs);
        
        checkOuputs();
        //Debug.Log(net.outputs[0].getActivation());

        if(player.dead){
            hasDied = true;
            player.rightThigh = false;
            player.rightThighEx = false;
            player.leftThigh = false;
            player.leftThighEx = false;
            player.rightLeg = false;
            player.rightLegEx = false;
            player.leftLeg = false;
            player.leftLegEx = false;
        }


    }
}
