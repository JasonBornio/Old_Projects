using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class groundCollider : MonoBehaviour
{
    //public Collider2D ground;
    //public Collider2D obejct;
    public bool isGrounded = false;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {

    }

    private void OnTriggerEnter2D(Collider2D collision)
    {
        if(collision.CompareTag("Ground")){
            //Debug.Log("GORUNNNND");
            isGrounded = true;
        }
    }

    private void OnTriggerStay2D(Collider2D collision){
        if(collision.CompareTag("Ground")){
            //Debug.Log("Still GORUNNNND");
        }
    }

    private void OnTriggerExit2D(Collider2D collision)
    {

        if(collision.CompareTag("Ground")){
            //Debug.Log("NOT GORUNNNND");
            isGrounded = false;
        }

    }
}
