using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Barrier : MonoBehaviour
{
    GameObject wall;
    public int speed = 1;
    public bool move = false;

    // Start is called before the first frame update
    void Start()
    {
        wall = GameObject.Find("Barrier");
        transform.position = new Vector3(-100f, transform.position.y, transform.position.z);
    }

    // Update is called once per frame
    void Update()
    {
        if(move){
            transform.position = new Vector3(transform.position.x + speed * Time.deltaTime, transform.position.y, transform.position.z);
        }
        
    }
}
