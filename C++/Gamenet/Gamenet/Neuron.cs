using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Gamenet
{
    internal class Neuron
    {
        private List<float> weights = new List<float>();
        private float activation = 0;
        private float bias = 0;
        private int weightsLength = 0;

        public void connect(List<Neuron> previousLayer)
        {
            float rand = 0f;
            weightsLength = previousLayer.size();
            for (int i = 0; i < weightsLength; i++)
            {
                weights.Add(Random.Range(-1.0f, 1.0f));
                //Debug.Log(weights);
            }
            bias = Random.Range(-1.0f, 1.0f);
        }

        public void calculate(List<Neuron> previousLayer)
        {
            float sum = 0;
            for (int i = 0; i < weightsLength; i++)
            {
                sum += previousLayer[i].getActivation() * weights[i];
            }
            activation = function(sum + bias);
        }

        public float function(float value)
        {
            return float(1 / (1 + Math.Exp(-value)));
        }

        public float getActivation()
        {
            return activation;
        }

        public float getWeight(int index)
        {
            return weights[index];
        }

    }

}
