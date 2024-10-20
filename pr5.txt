using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class scoller : MonoBehaviour
{
    public float speed =0.5f;


    // Start is called before the first frame update
    void Start()
    {
       
    }

    // Update is called once per frame
    void Update()
    {
        Vector2 offset = new Vector2(Time.time * speed, 0);
        Renderer renderer = GetComponent<Renderer>();

        if (renderer != null)
        {
            renderer.material.mainTextureOffset = offset;
        }
    }
}