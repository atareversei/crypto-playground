#include <stdio.h>
#include <stdlib.h>

void xor_files(const char *infile, const char *keyfile, const char *outfile) {
  FILE *in = fopen(infile, "rb");
  FILE *key = fopen(keyfile, "rb");
  FILE *out = fopen(outfile, "wb");

  if (!in || !key || !out) {
    perror("File open error");
    exit(1);
  }

  int byte_in, byte_key;
  while((byte_in = fgetc(in)) != EOF && (byte_key = fgetc(key)) != EOF) {
    fputc(byte_in ^ byte_key, out);
  }

  fclose(in);
  fclose(key);
  fclose(out);
}

// <e|d> is actually doing nothing, it is just there for the clarity of the script.
int main(int argc, char *argv[]) {
  if (argc != 5) {
    printf("Usage: %s <e|d> <input> <key> <output>", argv[0]);
    return 1;
  }

  xor_files(argv[2], argv[3], argv[4]);
  printf("Done. Output written to %s\n", argv[4]);
  return 0;
}