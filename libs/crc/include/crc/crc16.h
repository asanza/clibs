
#ifndef B0F04401_87E9_412E_934F_CC9B825D9DD0
#define B0F04401_87E9_412E_934F_CC9B825D9DD0

#include <stdint.h>

/**
 * @brief Calculate the crc16 as defined by modbus spec.
 * 
 * @param buf 
 * @param len 
 * @return uint16_t 
 */
uint16_t
crc16( uint8_t * buf, uint16_t len );

#endif /* B0F04401_87E9_412E_934F_CC9B825D9DD0 */
