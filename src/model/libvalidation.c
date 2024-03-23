#include <ctype.h>
#include <stdbool.h>
#include <string.h>

#define MAX_NAME_LENGTH 50

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

bool validate_name(const char *name) {
  int len = strlen(name);

  if (len > MAX_NAME_LENGTH) {
    return false;
  }

  bool first_char_seen = false;
  bool prev_char_was_space = false;

  for (int i = 0; i < len; i++) {
    char c = name[i];

    if (!isalpha(c) && c != ' ') {
      return false;
    }

    if (c == ' ' && prev_char_was_space) {
      return false;
    }

    if (c == ' ' && (i == 0 || i == len - 1)) {
      return false;
    }

    if (!first_char_seen && c != ' ') {
      first_char_seen = true;
    }

    prev_char_was_space = (c == ' ');
  }

  return first_char_seen;
}

bool validate_phone_number(const char *phone_number) {
  int len = strlen(phone_number);
  if (len != 11) {
    return false;
  }

  for (int i = 0; i < len; ++i) {
    if (!isdigit(phone_number[i])) {
      return false;
    }
  }

  if (phone_number[0] != '0' && phone_number[1] != '9') {
    return false;
  }

  return true;
}

bool validate_course(const char *course) {
  int len = strlen(course);

  if (len <= 2) {
    return false;
  }

  for (int i = 0; i < len; ++i) {
    if (course[i] == ' ') {
      return false;
    }

    if (!isalpha(course[i])) {
      return false;
    }
  }
  return true;
}

bool validate_section(const char *section) {
  int len = strlen(section);
  if (len != 1) {
    return false;
  }

  if (!isalpha(section[0])) {
    return false;
  }

  return true;
}
