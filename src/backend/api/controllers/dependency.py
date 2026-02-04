from src.backend.domain.ports.inside.OneTurnElectionPort import OneTurnElectionPort
from src.backend.domain.ports.inside.ProportionalNationalElectionPort import ProportionalNationalElectionPort
from src.backend.domain.ports.outside.ResultsElectionsPort import ResultsElectionsPort
from src.backend.domain.services.GlobalElection.BuildCongress import BuildCongress
from src.backend.domain.services.GlobalElection.TotalCongressPerson import TotalCongressPerson
from src.backend.domain.services.GlobalElection.SeatsResults import SeatsResults
from src.backend.domain.services.GlobalElection.RegroupCongressPersonsByParties import RegroupCongressPersonsByParties
from src.backend.domain.services.GlobalElection.RepresentativeCongress import RepresentativeCongress
from src.backend.domain.services.GlobalElection.CongressPersonElected import CongressPersonElected
from src.backend.domain.services.GlobalElection.StabilityCongress import StabilityCongress
from src.backend.domain.services.OneTurnElection.ConstructDepartmentalAssemblies import ConstructDepartmentalAssemblies
from src.backend.domain.services.OneTurnElection.OneTurnCongressPersonElectedByDpt import OneTurnCongressPersonElectedByDpt
from src.backend.domain.services.OneTurnElection.OneTurnElectionService import OneTurnElectionService
from src.backend.domain.services.ProportionalDepartmentElection.CongressPersonByDepartment import CongressPersonByDepartment
from src.backend.domain.services.ProportionalDepartmentElection.SeatDistributionRule import SeatDistributionRule
from src.backend.domain.services.ProportionalDepartmentElection.DistrictsVoteFromDpt import DistrictsVoteFromDpt
from src.backend.domain.services.ProportionalDepartmentElection.ManageCongressPersonsByDepartment import ManageCongressPersonsByDepartment
from src.backend.domain.services.ProportionalDepartmentElection.ModeDesignCongressPerson import ModeDesignCongressPerson
from src.backend.domain.services.ProportionalDepartmentElection.ProportionalDepartmentElectionService import ProportionalDepartmentElectionService
from src.backend.domain.services.ProportionalNationalElection.AllocateSeatsForParties import AllocateSeatsForParties
from src.backend.domain.services.ProportionalNationalElection.ProportionalNationalElectionService import ProportionalNationalElectionService
from src.backend.domain.services.ProportionalNationalElection.RemoveSmallParties import RemoveSmallParties
from src.backend.infrastructure.files.JsonFiles import JsonFiles
from src.backend.infrastructure.services.JsonResultsElection import JsonResultsElection

def get_one_turn_election_service() -> OneTurnElectionPort:
    json_service = __get_json_service()
    stability_congress = StabilityCongress(577)
    representative_congress = RepresentativeCongress(577)
    build_congress = BuildCongress(stability_congress, representative_congress)
    congress_person_elected = CongressPersonElected()
    one_turn_congress_person_elected_by_dpt = OneTurnCongressPersonElectedByDpt()
    contruct_departmental_assemblies = ConstructDepartmentalAssemblies()
    election = OneTurnElectionService(json_service, congress_person_elected, build_congress, one_turn_congress_person_elected_by_dpt, contruct_departmental_assemblies)
    return election

def get_proportional_national_election_service() -> ProportionalNationalElectionPort:
    json_service = __get_json_service()
    seats_results = SeatsResults()
    remove_small_parties = RemoveSmallParties()
    #TODO externalize conf
    allocate_seats_by_parties = AllocateSeatsForParties(577)
    select_congress_persons = CongressPersonElected()
    regroup_congress_persons_by_parties = RegroupCongressPersonsByParties()
    representative_congress = RepresentativeCongress(577)
    stability_congress = StabilityCongress(577)
    build_congress = BuildCongress(stability_congress, representative_congress)
    election = ProportionalNationalElectionService(json_service, seats_results, remove_small_parties, allocate_seats_by_parties, 
                                                   select_congress_persons, regroup_congress_persons_by_parties, build_congress)
    return election

def get_proportional_departmental_election_service () -> ProportionalDepartmentElectionService:
    mode = "proportionalDepartmental"
    json_service = __get_json_service()
    mode_design_congress_person = ModeDesignCongressPerson()
    districts_vote_from_dpt = DistrictsVoteFromDpt()
    seats_results = SeatsResults()        
    seat_distribution_rule = SeatDistributionRule()
    select_congress_persons = CongressPersonElected()
    regroup_congress_persons_by_parties = RegroupCongressPersonsByParties()
    total_congress_person = TotalCongressPerson()

    congress_persons_by_departments = CongressPersonByDepartment(mode_design_congress_person, districts_vote_from_dpt, seats_results, 
                                                                 seat_distribution_rule, select_congress_persons, 
                                                                 regroup_congress_persons_by_parties, total_congress_person, mode)
    manage_congress_persons_by_department = ManageCongressPersonsByDepartment()        
    stability_congress = StabilityCongress(577)
    representative_congress = RepresentativeCongress(577)
    build_congress = BuildCongress(stability_congress, representative_congress)
    proportional_department_election_service = ProportionalDepartmentElectionService(json_service, congress_persons_by_departments, manage_congress_persons_by_department, 
                                                                                        build_congress, mode)    
    return proportional_department_election_service

def __get_json_service() -> ResultsElectionsPort: 
    json_files = JsonFiles()
    json_service = JsonResultsElection(json_files)
    return json_service