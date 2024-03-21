#include <ctype.h>
#include <stdbool.h>
#include <string.h>

bool validate_id_number(const char *id_number) {
  int len = strlen(id_number);

  if (len != 11) {
    return false;
  }

  if (isdigit(id_number[0]) && isdigit(id_number[1]) && id_number[2] == '-' &&
      isdigit(id_number[3]) && id_number[4] == '-' && isdigit(id_number[5]) &&
      id_number[6] == '-' && isdigit(id_number[7]) && isdigit(id_number[8]) &&
      isdigit(id_number[9]) && isdigit(id_number[10])) {
    return true;
  }

  return false;
}

bool validate_phone_number(const char *phone_number) {
  int len = strlen(phone_number);
  if (len != 11) {
    return false;
  }

  for (int i = 0; i < len; i++) {
    if (!isdigit(phone_number[i])) {
      return false;
    }
  }

  if (phone_number[0] != '0' && phone_number[1] != '9') {
    return false;
  }

  return true;
}
