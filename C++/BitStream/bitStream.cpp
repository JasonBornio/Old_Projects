#include <pthread.h>
#include "bitStream.h"
#include "Transmitter.h"
#include "Reciver.h"
#include <Windows.h>
#include <cstdlib>
#include <unistd.h>

pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;
#define DELAY 100000

void* BitStream(void* bits)
{
	bitStream* iptr = (bitStream*)bits;
	while (1) {
		for (int i = 0; i < 8; i++) {
			usleep(DELAY);
			iptr->shift();
		}
		usleep(1000);
	}
}

void* BitStream2(void* bits) {
	bitStream* iptr = (bitStream*)bits;
	Transmitter x;
	while (1) {
		usleep(DELAY*8);
		x.set_value();
		for (int i = 0; i < 8; i++) {
			iptr->Byte[i] = x.Byte[i];
		}
		iptr->addByte();
		usleep(1000);
	}
}

int main() {

	bitStream bits;

	pthread_t worker_thread;
	pthread_create(&worker_thread, NULL, BitStream, &bits);
	pthread_create(&worker_thread, NULL, BitStream2, &bits);
	while (1) {
	}

}
