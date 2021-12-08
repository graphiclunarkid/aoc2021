use counter::Counter;

// Extremely n00b problem #1: all the example functions I can find use standard data types like i32
// or char.  This fails to compile because I can't figure out how to reference the data type of a
// Counter object (struct?) in the function declaration...
fn increment_day(s: Counter<&str>) -> Counter<&str> {
    s
}

fn print_type_of<T>(_: &T) {
    println!("{}", std::any::type_name::<T>())
}

fn main() {

    // Read puzzle input from file
    let input = include_str!("day6-input");

    // Convert input into a Counter object I don't understand <Counter<_>>() yet: I just stole it
    // from https://docs.rs/counter/latest/counter/
    let school = input.trim().split(',')
        .collect::<Counter<_>>();

    print_type_of(&school);
    
    let new_school = increment_day(&school);

    println!("   Today's school: {:?}", school);

    println!("Tomorrow's school: {:?}", new_school);
}
