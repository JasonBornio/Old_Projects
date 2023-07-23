#include "Network.h"

#pragma region publicFuncs

void clear() {
    COORD topLeft = { 0, 0 };
    HANDLE console = GetStdHandle(STD_OUTPUT_HANDLE);
    CONSOLE_SCREEN_BUFFER_INFO screen;
    DWORD written;

    GetConsoleScreenBufferInfo(console, &screen);
    FillConsoleOutputCharacterA(
        console, ' ', screen.dwSize.X * screen.dwSize.Y, topLeft, &written
    );
    FillConsoleOutputAttribute(
        console, FOREGROUND_GREEN | FOREGROUND_RED | FOREGROUND_BLUE,
        screen.dwSize.X * screen.dwSize.Y, topLeft, &written
    );
    SetConsoleCursorPosition(console, topLeft);
}


Network::Network(int inputs, int outputs, int num_layers, int layerNodes) {
    input_length = inputs;
    output_length = outputs;
    layers = num_layers;
    layer_length = layerNodes;
    Create();
}

Network::~Network() {

}

void Network::Train(vector<vector<float>> inputs, vector<vector<float>>labels, int iterations = 1, bool show = false) {
    
    for (int k = 0; k < iterations; k++) {
        
        vector<float> predictions;

        for (int i = 0; i < inputs.size(); i++) {
            predictions = FeedForward(inputs[i]);
            BackPropagate(predictions, labels[i]);

            if (show) {
                cout << "\n\nINPUTS:";
                for (int o = 0; o < inputs[i].size(); o++) {
                    cout << " " << inputs[i][o];
                }

                cout << "\nPREDICTIONS:";
                for (int o = 0; o < predictions.size(); o++) {
                    cout << " " << predictions[o];
                }
            }
            
        }
        
        if (show)
            cout << "\n--------------------------";
            
    }
}

#pragma endregion

#pragma region privateFuncs

void Network::Create() {

    for (int i = 0; i < input_length; i++) {
        Neuron node;
        input_nodes.push_back(node);
    }

    for (int j = 0; j < layers; j++) {

        vector<Neuron> intermediate;
        for (int i = 0; i < layer_length; i++) {
            Neuron node;
            intermediate.push_back(node);
        }
        layer_nodes.push_back(intermediate);
    }

    for (int i = 0; i < output_length; i++) {
        Neuron node;
        output_nodes.push_back(node);
    }

#pragma region connect

    if (layers > 0) {

        for (int j = 0; j < layers; j++) {

            if (j == 0) {
                for (int i = 0; i < layer_length; i++) {
                    layer_nodes[0][i].Connect(input_nodes);
                }
            }
            else {

                for (int i = 0; i < layer_length; i++) {
                    layer_nodes[j][i].Connect(layer_nodes[j - 1]);
                }
            }
        }

        for (int i = 0; i < output_length; i++) {
            output_nodes[i].Connect(layer_nodes[layers-1]);
        }

    }
    else {

        for (int i = 0; i < output_length; i++) {
            output_nodes[i].Connect(input_nodes);
        }

    }

#pragma endregion

}

vector<float> Network::FeedForward(vector<float> inputs) {

    vector<float> outputs;

    if (input_length != inputs.size()) {
        cout << "\nerror: " << "input vector length does not match input node length";
        return outputs;
    }

    //cout << "\ninputs: ";
    for (int i = 0; i < input_length; i++) {
        //cout << inputs[i];
        input_nodes[i].setActivation(inputs[i]);
    }

    if (layers > 0) {
        //cout << "\nlayers: ";
        for (int j = 0; j < layers; j++) {
            //cout << "\nhiddenNodes: ";
            if (j == 0) {
                for (int i = 0; i < layer_length; i++) {
                    layer_nodes[0][i].calculateActivation(input_nodes);
                    //cout << "\n" << layer_nodes[0][i].getActivation();
                }
            }
            else {
                for (int i = 0; i < layer_length; i++) {
                    layer_nodes[j][i].calculateActivation(layer_nodes[j - 1]);
                    //cout << "\n" << layer_nodes[j][i].getActivation();
                }
            }
        }
        //cout << "\noutputs: ";
        for (int i = 0; i < output_length; i++) {
            output_nodes[i].calculateActivation(layer_nodes[layers-1]);
            outputs.push_back(output_nodes[i].getActivation());
            //cout << "\n" << output_nodes[i].getActivation();
        }
    }

    else {
        //cout << "\noutputs: ";
        for (int i = 0; i < output_length; i++) {
            output_nodes[i].calculateActivation(input_nodes);
            //cout << "\n" << output_nodes[i].getActivation();
            outputs.push_back(output_nodes[i].getActivation());
            //output_nodes[i].showWeights();
        }
        
    }

    return outputs;

}

void Network::BackPropagate(vector<float> predictions, vector<float>labels) {

    float deltaCost;
    vector<float> deltaCs;
    //cout << "\nBack";

    if (layers > 0) {

        //OUTPUTS
        for (int i = 0; i < output_length; i++) {
            deltaCost = lossDerivative(predictions[i], labels[i]);
            output_nodes[i].calculateOutputGradients(layer_nodes[layers-1]);
            output_nodes[i].updateWeights(deltaCost, input_nodes);
            deltaCs.push_back(deltaCost);
        }

        //HIDDENS
        for (int j = 0; j < layers; j++) {
            if (j == 0) {
                if (j == layers - 1) {
                    for (int i = 0; i < output_length; i++) {
                        layer_nodes[j][i].calculateHiddenGradients(input_nodes, output_nodes, deltaCs);
                        layer_nodes[j][i].updateHiddenWeights(deltaCs);
                    }
                }
                else {

                    for (int i = 0; i < output_length; i++) {
                        layer_nodes[j][i].calculateHiddenGradients(input_nodes, layer_nodes[j + 1], deltaCs);
                        layer_nodes[j][i].updateHiddenWeights(deltaCs);
                    }

                }
            }
            else {
                if (j == layers - 1) {
                    for (int i = 0; i < output_length; i++) {
                        layer_nodes[j][i].calculateHiddenGradients(layer_nodes[j-1], output_nodes, deltaCs);
                        layer_nodes[j][i].updateHiddenWeights(deltaCs);
                    }
                }
                else {

                    for (int i = 0; i < output_length; i++) {
                        layer_nodes[j][i].calculateHiddenGradients(layer_nodes[j - 1], layer_nodes[j + 1], deltaCs);
                        layer_nodes[j][i].updateHiddenWeights(deltaCs);
                    }

                }
            }
        }
    }

    else {
        //OUTPUTS
        for (int i = 0; i < output_length; i++) {
            deltaCost = lossDerivative(predictions[i], labels[i]);
            output_nodes[i].calculateOutputGradients(input_nodes);
            output_nodes[i].updateWeights(deltaCost, input_nodes);
        }
    }
    //cout << "\nBackOut";

}

float Network::LossFucntion(vector<float> predictions, vector<float> labels) {

    float sum = 0;
    size_t size = labels.size();

    for (int i = 0; i < size; i++) {
        sum += float(pow((labels[i] - predictions[i]), 2));
    }

    return (1 / (2 * size)) * sum;
}

float Network::lossDerivative(float prediciton, float label) {
    return (prediciton - label);
}


float Network::nextSUM(vector<Neuron> nextLayer) {
    float sum = 0;

    //for (int i = 0; i < nextLayer[0].)
       // return sum;
    return  0;
}
#pragma endregion