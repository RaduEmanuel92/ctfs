/********************************************************************
 *   This C program was generated by spl2c, the Shakespeare to C    *
 *          converter by Jon Åslund and Karl Hasselström.           *
 ********************************************************************/

/* libspl definitions and function prototypes */
#include "spl.h"

int main(void)
{
  /******************************************************************
   * MUCH ADO ABOUT HACKING                                         *
   ******************************************************************/
  
  CHARACTER *benedick;                    /* a budding young hacker */
  CHARACTER *beatrice;                    /* a veteran exploiter */
  CHARACTER *don_pedro;                   /* a good friend of the others */
  CHARACTER *don_john;                    /* he is just kinda there */
  CHARACTER *achilles;                    /* I thought he was from Greece */
  CHARACTER *cleopatra;                   /* now this is just getting ridiculous */
  
  int comp1, comp2;
  
  global_initialize();
  
  benedick = initialize_character("Benedick");
  beatrice = initialize_character("Beatrice");
  don_pedro = initialize_character("Don Pedro");
  don_john = initialize_character("Don John");
  achilles = initialize_character("Achilles");
  cleopatra = initialize_character("Cleopatra");
  
  act_i:                                  /* Also the last act */
  
  act_i_scene_i:                          /* Benedick learns his place */
  
  enter_scene(15, beatrice);
  enter_scene(15, don_john);
  
  activate_character(20, beatrice);
  assign(18, second_person, 0); // don_john = 0
  
  exit_scene(20, don_john);
  
  enter_scene(21, don_pedro);
  
  activate_character(26, beatrice);
  assign(24, second_person, 0); // don_pedro = 0
  
  exit_scene(26, don_pedro);
  
  enter_scene(27, achilles);
  
  activate_character(32, beatrice);
  assign(30, second_person, 2*2*2*2*2*1); // achiles = 32
  
  exit_scene(32, achilles);
  
  enter_scene(33, cleopatra);
  
  activate_character(38, beatrice);
  assign(36, second_person, int_sub(36, 2*2*2*2*2*2*2*1, achilles->value)); //cleopatra = 128 - achiles = 128 - 32
  
  exit_scene(38, cleopatra);
  
  enter_scene(39, benedick);
  
  activate_character(44, beatrice);
  assign(42, second_person, 0); // benedick = 0
  
  act_i_scene_ii:                         /* Benedick strengthens his memory */
  
  activate_character(49, beatrice);
  char_input(47, second_person); //benedick = getchar()
  push(47, second_person, value_of(47, second_person));
  
  activate_character(53, benedick);
  assign(50, second_person, int_add(50, value_of(50, second_person), 1)); //beatrice += 1
  comp1 = value_of(51, first_person); // benedick
  comp2 = 2*2*2*2*2*1; // 32 (in this case numerical representation of char ' ' space)
  truth_flag = (comp1 == comp2); // benedick == 32
  
  activate_character(56, beatrice);
  if (!truth_flag) {
    goto act_i_scene_ii; // reads all chars until the first space
  }
  
  activate_character(59, benedick);
  assign(57, second_person, int_add(57, value_of(57, second_person), (-1))); //beatrice -= 1
  
  activate_character(62, beatrice);
  pop(60, second_person);
  
  act_i_scene_iii:                        /* Benedick teaches his friends about hacking */
  
  activate_character(67, beatrice);
  pop(65, second_person); // benedick = a char from input (don't know if it starts from beginning or end, will find out)
  assign(65, second_person, int_sub(65, value_of(65, second_person), achilles->value)); // benedick -= achilles
  
  activate_character(70, benedick);
  assign(68, second_person, int_add(68, value_of(68, second_person), (-1))); // beatrice -= 1
  
  exit_scene(70, beatrice);
  
  enter_scene(71, don_john);
  
  activate_character(76, benedick);
  assign(74, second_person, value_of(74, first_person)); // don_john = benedick
  
  exit_scene(76, don_john);
  
  enter_scene(77, don_pedro);
  
  activate_character(83, don_pedro);
  assign(80, second_person, int_add(80, value_of(80, second_person), value_of(80, first_person))); // don_pedro += benedick
  assign(81, second_person, int_mod(81, value_of(81, second_person), cleopatra->value)); // benedick %= cleopatra
  
  exit_scene(83, benedick);
  
  enter_scene(84, don_john);
  
  activate_character(89, don_john);
  assign(87, second_person, value_of(87, first_person)); // don_pedro = don_john
  
  exit_scene_all(89);
  
  enter_scene(90, beatrice);
  enter_scene(90, benedick);
  
  activate_character(95, beatrice);
  assign(93, second_person, int_add(93, value_of(93, second_person), achilles->value)); // benedick += achilles
  char_output(93, second_person); // print benedick
  
  activate_character(98, benedick);
  comp1 = value_of(96, second_person); // beatrice
  comp2 = 0;
  truth_flag = (comp1 > comp2); // beatrice > 0 //end of input string
  
  activate_character(101, beatrice);
  if (truth_flag) {
    goto act_i_scene_iii; //loops scene 3 until there are no chars left
  }
  
  exit_scene_all(101);
  
  return 0;
}
