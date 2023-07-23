
using System;
using System.Collections;
using UnityEngine;
using System.Collections.Generic;

public class Movement : MonoBehaviour
{
    public float JumpHeight = 5f;
    public float DoubleJumpHeight = 3.5f;
    public float Speed = 1f;
    private Rigidbody rb;
    public float groundHeight = 0.1001f;
    public bool grounded;
    public bool airTime;
    public float timeT;
    

    // Start is called before the first frame update
    void Start()
    {
        rb = GetComponent<Rigidbody>();
    }

    // Update is called once per frame
    void Update()
    {
        checkGrounded();
        if (Input.GetKeyDown("space") && grounded)
        {
            jump();
        }
        else if(Input.GetKeyDown("space") && airTime)
        {
            doubleJump();
        }
        else if (!airTime)
        {
            move();
        }
    }


    void checkGrounded()
    {
        RaycastHit hit;
        Vector3 vector = new Vector3(0, -0.4f, 0);
        Ray landingRay = new Ray(transform.position + vector, Vector3.down);
        if (Physics.Raycast(landingRay, out hit, groundHeight)){
            grounded = true;
            airTime = false;
            Debug.DrawRay(transform.position + vector, Vector3.down * groundHeight, Color.green);
        }
        else
        {
            grounded = false;
            Debug.DrawRay(transform.position + vector, Vector3.down * groundHeight, Color.red);
        }
    }
    

    void jump()
    {
        airTime = true;
        Vector3 jump = new Vector3(0, 1, 0);
        rb.velocity = jump /* Time.deltaTime*/ * JumpHeight;
        print("Jumped");
        float moveHorizontal = Input.GetAxis("Horizontal");

        Vector3 movement = new Vector3(1 * moveHorizontal * Speed, 0, 0);

        movement *= Time.deltaTime;

        transform.Translate(movement);
    }

    void doubleJump()
    {
        airTime = false;
        Vector3 jump = new Vector3(0, 1, 0);
        rb.velocity = jump /* Time.deltaTime*/ * DoubleJumpHeight;
        print("DoubleJump");
        float moveHorizontal = Input.GetAxis("Horizontal");

        Vector3 movement = new Vector3(1 * moveHorizontal * Speed, 0, 0);

        movement *= Time.deltaTime;

        transform.Translate(movement);
    }

    void move()
    {

        if (Input.GetAxis("Horizontal") != 0)
        {
            Debug.Log("pressed");
            timeT = Time.deltaTime;
            Debug.Log("time = " + timeT);
            
        }

        float moveHorizontal = Input.GetAxis("Horizontal");
        
        Vector3 movement = new Vector3(1 * moveHorizontal * Speed, 0, 0);


        movement *= Time.deltaTime;

        transform.Translate(movement);
    }
}
