using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Muscle : MonoBehaviour
{
    public DistanceJoint2D joint;
    public Muscle partnerJoint; 
    public float force = 1;
    public bool contract = false;
    public bool extend = false;
    public bool extending = false;


    // Start is called before the first frame update
    void Start()
    {
        joint.distance = 0;
        joint.enabled = false;
        joint.autoConfigureDistance = true;
        joint.enableCollision = true;
    }

    // Update is called once per frame
    void Update()
    {
        if(contract){
            joint.enabled = true;
            joint.autoConfigureDistance = false;
            if (joint.distance < 0.0001){
                joint.distance = 0;
                partnerJoint.extend = false;
            }
            else{
                joint.distance = joint.distance - (joint.distance * 0.05f * force);
                partnerJoint.extend = true;
            }
        }
        else if(extend){
            joint.enabled = true;
            joint.autoConfigureDistance = false;
            joint.distance = joint.distance + ((1/joint.distance) * 0.05f * force);
            
        }
        else{
            joint.enabled = false;
            joint.autoConfigureDistance = true;
            partnerJoint.extend = false;
        }
        extending = partnerJoint.extend;

    }
}
